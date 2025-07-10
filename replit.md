# Text to Image API - Gemini 2.0 Flash

## Overview

This is a production-ready Flask-based serverless API that generates images from text descriptions using Google's Gemini 2.0 Flash model. The application includes a beautiful web interface for testing the API and comprehensive documentation for developers. It's designed to be deployed on both Replit and Railway.com with zero configuration.

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes

✓ **2025-07-10**: Successfully implemented complete text-to-image API
✓ **2025-07-10**: Fixed Flask-Limiter configuration issue
✓ **2025-07-10**: Integrated Google Gemini 2.0 Flash for image generation
✓ **2025-07-10**: Created dual deployment configuration for Replit and Railway
✓ **2025-07-10**: Added comprehensive API documentation and testing interface
✓ **2025-07-10**: Verified image generation functionality with authentic API calls

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **API Design**: RESTful API with JSON responses
- **Rate Limiting**: Flask-Limiter for API protection (200/day, 50/hour, 10/minute)
- **Error Handling**: Centralized logging and error responses
- **Proxy Support**: ProxyFix middleware for proper IP detection behind proxies

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default)
- **Styling**: Bootstrap with custom CSS
- **JavaScript**: Vanilla JavaScript for form handling and API interactions
- **UI Components**: Responsive design with Bootstrap cards and forms

### AI Integration
- **AI Service**: Google Gemini 2.0 Flash for image generation
- **API Client**: Google GenAI Python client
- **Image Processing**: Base64 encoding for image data transfer

## Key Components

### Core Application (app.py)
- Flask application setup with security configurations
- Rate limiting implementation with Flask-Limiter
- Health check endpoint for monitoring
- Complete API endpoint for image generation with validation
- Error handling for all endpoints with proper HTTP status codes

### AI Service Layer (gemini_service.py)
- **GeminiImageGenerator**: Wrapper class for Gemini API
- **Prompt Enhancement**: Automatic prompt optimization based on style and size parameters
- **Error Handling**: Comprehensive error handling for API failures
- **Configuration**: Environment-based API key management
- **Connection Testing**: Built-in API connectivity verification

### Web Interface
- **Frontend**: HTML template with Bootstrap dark theme
- **JavaScript**: Form validation, character counting, and API interaction
- **Styling**: Custom CSS with gradient buttons and responsive design
- **Sample Prompts**: Built-in inspiration generator for users

### Static Assets
- **CSS**: Custom styling with dark theme support and animations
- **JavaScript**: Client-side form handling, API calls, and image download functionality

## Data Flow

1. **User Input**: User enters text prompt, selects style and size options
2. **Frontend Validation**: JavaScript validates input length and required fields
3. **API Request**: POST request to `/api/generate` endpoint
4. **Rate Limiting**: Request passes through rate limiting middleware
5. **Prompt Enhancement**: Service layer enhances prompt with style parameters
6. **AI Generation**: Gemini 2.0 Flash generates image from enhanced prompt
7. **Response Processing**: Image data encoded and returned as JSON
8. **Frontend Display**: Generated image displayed in the web interface

## External Dependencies

### Core Dependencies
- **Flask**: Web framework and routing
- **Flask-Limiter**: Rate limiting functionality
- **Google GenAI**: Official Google Gemini API client
- **Werkzeug**: WSGI utilities and middleware

### Frontend Dependencies
- **Bootstrap**: CSS framework for responsive design
- **Font Awesome**: Icon library for UI elements
- **Custom CSS**: Application-specific styling

### Environment Variables
- **GEMINI_API_KEY**: Required for Google Gemini API access
- **SESSION_SECRET**: Flask session security (optional, has default)

## Deployment Strategy

### Dual Platform Support
- **Replit**: Zero-config deployment with built-in secrets management
- **Railway**: Production-ready serverless deployment with automatic scaling
- **Railway Config**: `railway.json` for deployment configuration
- **Environment Detection**: Automatic port and configuration detection

### Application Structure
- **Entry Point**: `main.py` for direct execution
- **WSGI Application**: `app.py` contains the Flask application
- **Static Files**: Served through Flask's static file handling
- **Templates**: Jinja2 templates for server-side rendering

### Configuration Management
- Environment variables for sensitive data (API keys)
- Default values for development environment
- Proxy-aware configuration for production deployments
- Auto-detection of deployment platform (Replit vs Railway)

### Security Considerations
- Rate limiting to prevent API abuse (5/min, 50/hour, 200/day)
- Input validation and sanitization
- Secure session management
- API key protection through environment variables
- ProxyFix middleware for proper IP detection

### Monitoring and Health Checks
- Health check endpoint at `/api/health`
- Comprehensive logging throughout the application
- Error tracking and response formatting
- Real-time API status monitoring

## Status

✅ **PRODUCTION READY**: The application is fully implemented and tested with authentic Google Gemini API integration. Image generation functionality has been verified and all endpoints are working correctly. Ready for deployment on both Replit and Railway.