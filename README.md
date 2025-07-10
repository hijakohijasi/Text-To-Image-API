# Text to Image API - Gemini 2.0 Flash

A Flask-based serverless API that generates images from text prompts using Google's Gemini 2.0 Flash model. Deployable on both Replit and Railway.

## Features

- **AI-Powered Image Generation**: Uses Google Gemini 2.0 Flash for high-quality image generation
- **Multiple Styles**: Realistic, Artistic, Cartoon, Digital Art, and 3D Render
- **Multiple Sizes**: Small (512x512), Medium (1024x1024), Large (1536x1536)
- **Rate Limiting**: Built-in protection against API abuse
- **Web Interface**: Beautiful testing interface with real-time preview
- **Dual Deployment**: Works on both Replit and Railway

## API Endpoints

### `GET|POST /api/generate`
Generate an image from text prompt. Supports both GET and POST methods.

**GET Request:**
```
GET /api/generate?prompt=A%20serene%20mountain%20landscape%20at%20sunset&style=realistic&size=medium
```

**POST Request:**
```json
{
  "prompt": "A serene mountain landscape at sunset",
  "style": "realistic",
  "size": "medium"
}
```

**Response:**
```json
{
  "success": true,
  "image": "base64_encoded_image_data",
  "prompt": "A serene mountain landscape at sunset",
  "style": "realistic",
  "size": "medium",
  "generated_at": 1752181804.6009817
}
```

### `GET /api/health`
Health check endpoint.

### `GET /api/styles`
Get available image styles.

### `GET /api/sizes`
Get available image sizes.

## Rate Limits

- 5 requests per minute for image generation
- 50 requests per hour
- 200 requests per day

## Environment Variables

- `GEMINI_API_KEY`: Required. Get from [Google AI Studio](https://aistudio.google.com)
- `SESSION_SECRET`: Optional. Flask session secret key
- `PORT`: Optional. Port to run on (defaults to 5000)

## Deployment

### Deploy on Replit

1. Fork this repository on Replit
2. Add your `GEMINI_API_KEY` to Replit Secrets
3. Click "Run" - that's it!

### Deploy on Railway

1. Connect your GitHub repository to Railway
2. Add `GEMINI_API_KEY` environment variable
3. Railway will automatically detect the `Procfile` and deploy

**Files needed for Railway:**
- `Procfile` (already included)
- `railway-requirements.txt` (copy to `requirements.txt` on Railway)
- Auto port detection via `PORT` environment variable

Alternatively, use the Railway CLI:
```bash
railway login
railway init
railway up
```

**Note:** Copy `railway-requirements.txt` to `requirements.txt` for Railway deployment.

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

3. Run the application:
```bash
python main.py
```

## Architecture

- **Backend**: Flask with Gunicorn
- **AI Service**: Google Gemini 2.0 Flash
- **Frontend**: Bootstrap + Vanilla JavaScript
- **Rate Limiting**: Flask-Limiter
- **Deployment**: Containerless serverless

## Usage Example

### GET Method
```python
import requests
import base64

# Generate image with GET
response = requests.get(
    "https://your-api-url.com/api/generate",
    params={
        "prompt": "A magical forest with glowing mushrooms",
        "style": "artistic",
        "size": "medium"
    }
)

data = response.json()
if data.get("success"):
    # Decode base64 image
    image_data = base64.b64decode(data["image"])
    with open("generated_image.png", "wb") as f:
        f.write(image_data)
```

### POST Method
```python
import requests
import base64

# Generate image with POST
response = requests.post(
    "https://your-api-url.com/api/generate",
    json={
        "prompt": "A magical forest with glowing mushrooms",
        "style": "artistic",
        "size": "medium"
    }
)

data = response.json()
if data.get("success"):
    # Decode base64 image
    image_data = base64.b64decode(data["image"])
    with open("generated_image.png", "wb") as f:
        f.write(image_data)
```

## License

MIT License