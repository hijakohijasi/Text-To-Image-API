from setuptools import setup, find_packages

setup(
    name="text-to-image-api",
    version="1.0.0",
    description="A Flask-based text-to-image API using Google Gemini 2.0 Flash",
    packages=find_packages(),
    install_requires=[
        "Flask==3.0.3",
        "flask-limiter==3.8.0", 
        "google-genai==0.3.0",
        "gunicorn==23.0.0",
        "werkzeug==3.0.4"
    ],
    python_requires=">=3.11",
)