# Text to Image API - Gemini 2.0 Flash

## Overview

This repository contains a Flask-based serverless API that generates images from text prompts using Google's Gemini 2.0 Flash model. The application provides a clean web interface for testing and offers REST API endpoints for programmatic access. It's designed to be deployable on both Replit and Railway platforms.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **API Design**: RESTful API with both GET and POST support
- **Rate Limiting**: Flask-Limiter for API abuse protection
- **Proxy Support**: ProxyFix middleware for proper IP detection behind proxies
- **Logging**: Built-in Python logging for debugging and monitoring

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default templating)
- **Styling**: Bootstrap with custom CSS for modern UI
- **JavaScript**: Vanilla JavaScript for form handling and API interactions
- **Real-time Features**: Character counting, loading states, and error handling

### AI Integration
- **Model**: Google Gemini 2.0 Flash for image generation
- **Service Layer**: Dedicated `GeminiImageGenerator` class for AI operations
- **Prompt Enhancement**: Automatic style and quality enhancement for better results

## Key Components

### Core Application Files
- `app.py`: Main Flask application with route definitions and middleware setup
- `gemini_service.py`: Service class handling Gemini AI integration
- `main.py`: Application entry point for deployment

### Frontend Components
- `templates/index.html`: Main web interface with testing form
- `static/script.js`: Client-side JavaScript for form handling
- `static/style.css`: Custom styling for enhanced UI

### Configuration Files
- `railway.json`: Railway deployment configuration
- `railway-requirements.txt`: Python dependencies for Railway deployment

## Data Flow

1. **User Request**: User submits text prompt via web interface or API endpoint
2. **Validation**: Flask validates input parameters (prompt, style, size)
3. **Rate Limiting**: Request checked against rate limits (5 per minute, 50 per hour, 200 per day)
4. **Prompt Enhancement**: Service layer enhances prompt with style and quality indicators
5. **AI Generation**: Gemini 2.0 Flash processes enhanced prompt and generates image
6. **Response**: Base64-encoded image data returned to client
7. **Display**: Web interface displays generated image or API returns JSON response

## External Dependencies

### AI Services
- **Google Gemini API**: Core image generation service
- **API Key**: Required environment variable `GEMINI_API_KEY`

### Python Libraries
- **Flask**: Web framework and routing
- **flask-limiter**: Rate limiting functionality
- **google-genai**: Official Google Gemini client library
- **werkzeug**: WSGI utilities and proxy handling
- **gunicorn**: WSGI HTTP server for production deployment

### Frontend Dependencies
- **Bootstrap**: UI framework via CDN
- **Font Awesome**: Icons via CDN
- **Custom CSS**: Enhanced styling for better user experience

## Deployment Strategy

### Multi-Platform Support
- **Replit**: Direct Flask development and hosting
- **Railway**: Production deployment with Nixpacks builder

## Recent Changes

✓ **2025-07-10**: Successfully implemented complete text-to-image API
✓ **2025-07-10**: Fixed Flask-Limiter configuration issue
✓ **2025-07-10**: Integrated Google Gemini 2.0 Flash for image generation
✓ **2025-07-10**: Created dual deployment configuration for Replit and Railway
✓ **2025-07-10**: Added comprehensive API documentation and testing interface
✓ **2025-07-10**: Verified image generation functionality with authentic API calls
✓ **2025-07-10**: Added GET method support for image generation API
✓ **2025-07-10**: Created Railway deployment files (Procfile, railway-requirements.txt)
✓ **2025-07-10**: Implemented auto port detection for multiple platforms
✓ **2025-07-10**: Updated documentation with GET and POST examples
✓ **2025-07-10**: Modified API to use GET method only with aspect ratio support
✓ **2025-07-10**: Added screen ratio options (1:1, 16:9, 9:16, 4:3, 3:4, 21:9)
✓ **2025-07-10**: Implemented HD quality image generation as default
✓ **2025-07-10**: Updated frontend interface to use new ratio parameter

## Current Status

✅ **PRODUCTION READY**: The application is fully functional with GET-only API method. All deployment files are configured for both Replit and Railway platforms. The API generates HD quality images with multiple aspect ratio options using Google Gemini 2.0 Flash with authentic API integration.

### Configuration Management
- **Environment Variables**: API keys and secrets managed via platform-specific methods
- **Rate Limiting**: In-memory storage for development, can be extended for production
- **Logging**: Configurable logging levels for debugging and monitoring

### Production Considerations
- **Gunicorn**: WSGI server for Railway deployment
- **Restart Policy**: Automatic restart on failure with retry limits
- **Port Binding**: Dynamic port allocation for cloud deployment
- **Proxy Headers**: Proper handling of forwarded headers for IP detection

### API Features
- **Multiple Endpoints**: Health check, image generation, style listing, and ratio listing
- **GET Method Only**: Simplified API with URL parameter support
- **Error Handling**: Comprehensive error responses and logging
- **Response Format**: Consistent JSON structure with metadata
- **HD Quality**: All images generated in high definition quality
- **Aspect Ratio Options**: Square (1:1), Landscape (16:9), Portrait (9:16), Standard (4:3), Portrait Standard (3:4), Ultra Wide (21:9)
- **Style Options**: Realistic, Artistic, Cartoon, Digital Art, and 3D Render