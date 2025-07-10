import os
import logging
from google import genai
from google.genai import types
from io import BytesIO
import time

logger = logging.getLogger(__name__)

class GeminiImageGenerator:
    """Service class for generating images using Google Gemini 2.0 Flash"""
    
    def __init__(self):
        """Initialize the Gemini client"""
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        
        self.client = genai.Client(api_key=api_key)
        logger.info("Gemini client initialized successfully")
    
    def generate_image(self, prompt: str, style: str = "realistic", size: str = "medium") -> bytes:
        """
        Generate an image from a text prompt using Gemini 2.0 Flash
        
        Args:
            prompt: Text description of the image to generate
            style: Style of the image (realistic, artistic, cartoon, etc.)
            size: Size of the image (small, medium, large)
            
        Returns:
            bytes: Generated image data
        """
        try:
            # Enhance prompt with style and quality indicators
            enhanced_prompt = self._enhance_prompt(prompt, style, size)
            
            logger.info(f"Generating image with enhanced prompt: {enhanced_prompt[:100]}...")
            
            # Generate content using Gemini 2.0 Flash with image generation
            response = self.client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=enhanced_prompt,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE'],
                    temperature=0.7,
                    max_output_tokens=1024
                )
            )
            
            # Extract image data from response
            if not response.candidates:
                logger.error("No candidates returned from Gemini API")
                return None
            
            content = response.candidates[0].content
            if not content or not content.parts:
                logger.error("No content parts returned from Gemini API")
                return None
            
            # Look for image data in the response parts
            for part in content.parts:
                if part.text:
                    logger.info(f"Generated text: {part.text[:100]}...")
                elif part.inline_data and part.inline_data.data:
                    logger.info("Image data found in response")
                    return part.inline_data.data
            
            logger.error("No image data found in response")
            return None
            
        except Exception as e:
            logger.error(f"Error generating image: {str(e)}")
            raise Exception(f"Failed to generate image: {str(e)}")
    
    def _enhance_prompt(self, prompt: str, style: str, size: str) -> str:
        """
        Enhance the user prompt with style and quality indicators
        
        Args:
            prompt: Original user prompt
            style: Desired style
            size: Desired size
            
        Returns:
            str: Enhanced prompt
        """
        style_modifiers = {
            "realistic": "photorealistic, high quality, detailed, professional photography",
            "artistic": "artistic, creative, expressive, painterly style",
            "cartoon": "cartoon style, animated, colorful, fun",
            "digital_art": "digital art, concept art, detailed, vibrant colors",
            "3d": "3D rendered, high quality 3D art, detailed modeling"
        }
        
        size_modifiers = {
            "small": "square format",
            "medium": "high resolution, square format",
            "large": "ultra high resolution, detailed, square format"
        }
        
        # Build enhanced prompt
        enhanced = f"{prompt}"
        
        # Add style modifier
        if style in style_modifiers:
            enhanced += f", {style_modifiers[style]}"
        
        # Add size modifier
        if size in size_modifiers:
            enhanced += f", {size_modifiers[size]}"
        
        # Add general quality modifiers
        enhanced += ", high quality, well composed, clear details"
        
        return enhanced
    
    def test_connection(self) -> bool:
        """
        Test the connection to Gemini API
        
        Returns:
            bool: True if connection is successful
        """
        try:
            # Try a simple text generation to test the connection
            response = self.client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents="Hello, world!",
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT'],
                    max_output_tokens=10
                )
            )
            
            return response.candidates is not None and len(response.candidates) > 0
            
        except Exception as e:
            logger.error(f"Connection test failed: {str(e)}")
            return False
