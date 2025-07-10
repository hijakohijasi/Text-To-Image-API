# Deployment Guide

This guide covers how to deploy the Text-to-Image API to different platforms.

## Railway.com Deployment

### Quick Deploy
1. Fork this repository
2. Connect your Railway account to GitHub
3. Create a new Railway project from your forked repository
4. Add the `GEMINI_API_KEY` environment variable
5. Deploy!

### Manual Configuration (if needed)

If you encounter build issues, Railway should automatically detect the Python project. The key files for Railway deployment are:

- `nixpacks.toml` - Build configuration
- `railway.json` - Railway-specific deployment settings
- `railway-requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification

### Environment Variables
Set these in your Railway project:
- `GEMINI_API_KEY` - Your Google Gemini API key

### Build Process
Railway will automatically:
1. Detect Python 3.11 from `runtime.txt`
2. Install dependencies from `railway-requirements.txt`
3. Start the application with Gunicorn

## Replit Deployment

### Quick Deploy
1. Import this repository to Replit
2. Add `GEMINI_API_KEY` to Secrets
3. Click Run

### Files for Replit
- `main.py` - Application entry point
- `replit.nix` - Nix configuration (if needed)
- `.replit` - Replit configuration

## Environment Variables Required

Both platforms need:
- `GEMINI_API_KEY` - Your Google Gemini API key from Google AI Studio

## Troubleshooting

### Railway Build Errors
If you get dependency errors:
1. Check that `railway-requirements.txt` has the correct package versions
2. Verify `nixpacks.toml` is properly configured
3. Check that `runtime.txt` specifies the correct Python version

### Common Issues
- **Build fails**: Check Python version compatibility
- **Import errors**: Verify all dependencies are listed in requirements files
- **API errors**: Ensure `GEMINI_API_KEY` is properly set

## API Endpoints
Once deployed, your API will be available at:
- `GET /` - Web interface
- `GET /api/generate` - Generate images
- `GET /api/health` - Health check
- `GET /api/styles` - Available styles
- `GET /api/ratios` - Available aspect ratios

## Performance Notes
- Images are generated on-demand (no caching)
- Rate limiting is enforced (5 requests/minute)
- HD quality images may take 3-8 seconds to generate