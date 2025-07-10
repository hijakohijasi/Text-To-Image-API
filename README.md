# Text to Image API - Gemini 2.0 Flash

A Flask-based serverless API that generates images from text prompts using Google's Gemini 2.0 Flash model. Deployable on both Replit and Railway.

## Features

- **HD Quality Images**: All images generated in high definition automatically
- **Multiple Aspect Ratios**: Square, landscape, portrait, and cinematic formats
- **Various Styles**: Realistic, artistic, cartoon, digital art, and 3D render
- **GET-Only API**: Simple URL-based requests for easy integration
- **Rate Limiting**: Built-in protection against API abuse
- **Web Interface**: Beautiful testing interface with real-time preview
- **Dual Deployment**: Works on both Replit and Railway

## API Endpoints

### `GET /api/generate`
Generate an HD image from text prompt using GET method only.

**Request:**
```
GET /api/generate?prompt=A%20serene%20mountain%20landscape%20at%20sunset&style=realistic&ratio=16:9
```

**Response:**
```json
{
  "success": true,
  "image": "base64_encoded_image_data",
  "prompt": "A serene mountain landscape at sunset",
  "style": "realistic",
  "ratio": "16:9",
  "quality": "HD",
  "generated_at": 1752181804.6009817
}
```

### `GET /api/health`
Health check endpoint.

### `GET /api/styles`
Get available image styles.

### `GET /api/ratios`
Get available aspect ratios and their descriptions.

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

```python
import requests
import base64

# Generate HD image with aspect ratio
response = requests.get(
    "https://your-api-url.com/api/generate",
    params={
        "prompt": "A magical forest with glowing mushrooms",
        "style": "artistic",
        "ratio": "16:9"  # Landscape HD format
    }
)

data = response.json()
if data.get("success"):
    # Decode base64 image
    image_data = base64.b64decode(data["image"])
    with open("generated_image.png", "wb") as f:
        f.write(image_data)
    
    print(f"Generated {data['quality']} quality image in {data['ratio']} aspect ratio")
```

## Supported Aspect Ratios

- **1:1** - Square (1024x1024) - Perfect for Instagram posts
- **16:9** - Landscape (1920x1080) - YouTube thumbnails, presentations  
- **9:16** - Portrait (1080x1920) - Instagram stories, mobile wallpapers
- **4:3** - Standard (1440x1080) - Classic photo format
- **3:4** - Portrait Standard (1080x1440) - Print-ready portraits
- **21:9** - Ultra Wide (2560x1080) - Cinematic, banner images

## License

MIT License