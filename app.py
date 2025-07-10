import os
import logging
import time
from flask import Flask, request, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.middleware.proxy_fix import ProxyFix
from gemini_service import GeminiImageGenerator
import base64
from io import BytesIO

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# Add proxy fix for proper IP detection behind proxies
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour", "10 per minute"],
    storage_uri="memory://",
)
limiter.init_app(app)

# Initialize Gemini service
gemini_service = GeminiImageGenerator()

@app.route('/')
def index():
    """Serve the main documentation and testing interface"""
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        "status": "healthy",
        "timestamp": time.time(),
        "service": "text-to-image-api",
        "version": "1.0.0"
    })

@app.route('/api/generate', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def generate_image():
    """Generate an image from a text prompt"""
    try:
        # Handle both GET and POST requests
        if request.method == 'GET':
            prompt = request.args.get('prompt', '').strip()
            style = request.args.get('style', 'realistic')
            size = request.args.get('size', 'medium')
        else:
            # POST method - validate JSON
            if not request.json:
                return jsonify({
                    "error": "Invalid request format",
                    "message": "Request must contain JSON data"
                }), 400
            
            prompt = request.json.get('prompt', '').strip()
            style = request.json.get('style', 'realistic')
            size = request.json.get('size', 'medium')
        
        if not prompt:
            return jsonify({
                "error": "Missing prompt",
                "message": "Please provide a text prompt for image generation"
            }), 400
        
        if len(prompt) > 1000:
            return jsonify({
                "error": "Prompt too long",
                "message": "Prompt must be less than 1000 characters"
            }), 400
        
        logger.info(f"Generating image for prompt: {prompt[:50]}...")
        
        # Generate image using Gemini
        image_data = gemini_service.generate_image(prompt, style, size)
        
        if not image_data:
            return jsonify({
                "error": "Generation failed",
                "message": "Failed to generate image. Please try again."
            }), 500
        
        # Convert image to base64
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        
        return jsonify({
            "success": True,
            "image": image_base64,
            "prompt": prompt,
            "style": style,
            "size": size,
            "generated_at": time.time()
        })
        
    except Exception as e:
        logger.error(f"Error generating image: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "message": "An unexpected error occurred during image generation"
        }), 500

@app.route('/api/styles')
def get_styles():
    """Get available image styles"""
    return jsonify({
        "styles": [
            {"id": "realistic", "name": "Realistic", "description": "Photorealistic images"},
            {"id": "artistic", "name": "Artistic", "description": "Artistic and creative style"},
            {"id": "cartoon", "name": "Cartoon", "description": "Cartoon and animated style"},
            {"id": "digital_art", "name": "Digital Art", "description": "Digital artwork style"},
            {"id": "3d", "name": "3D Render", "description": "3D rendered images"}
        ]
    })

@app.route('/api/sizes')
def get_sizes():
    """Get available image sizes"""
    return jsonify({
        "sizes": [
            {"id": "small", "name": "Small", "description": "512x512 pixels"},
            {"id": "medium", "name": "Medium", "description": "1024x1024 pixels"},
            {"id": "large", "name": "Large", "description": "1536x1536 pixels"}
        ]
    })

@app.errorhandler(429)
def rate_limit_exceeded(e):
    """Handle rate limit exceeded errors"""
    return jsonify({
        "error": "Rate limit exceeded",
        "message": "Too many requests. Please try again later."
    }), 429

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({
        "error": "Not found",
        "message": "The requested endpoint was not found"
    }), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle internal server errors"""
    logger.error(f"Internal server error: {str(e)}")
    return jsonify({
        "error": "Internal server error",
        "message": "An unexpected error occurred"
    }), 500

if __name__ == '__main__':
    # Auto port detection for different deployment environments
    port = int(os.environ.get('PORT', 5000))  # Railway and other services use PORT
    
    # Replit detection
    if os.environ.get('REPL_ID'):  # Replit environment
        port = 8080
    
    # Heroku detection
    if os.environ.get('DYNO'):  # Heroku environment
        port = int(os.environ.get('PORT', 5000))
    
    logger.info(f"Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
