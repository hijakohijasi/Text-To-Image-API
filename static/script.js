// Text to Image API - Frontend JavaScript

let currentImageData = null;

document.addEventListener('DOMContentLoaded', function() {
    // Form submission handler
    document.getElementById('generateForm').addEventListener('submit', handleGenerate);
    
    // Character counter for prompt
    const promptTextarea = document.getElementById('prompt');
    promptTextarea.addEventListener('input', updateCharacterCount);
    
    // Add character counter display
    const charCountDisplay = document.createElement('div');
    charCountDisplay.className = 'form-text';
    charCountDisplay.id = 'charCount';
    promptTextarea.parentNode.insertBefore(charCountDisplay, promptTextarea.nextSibling);
    updateCharacterCount();
});

function updateCharacterCount() {
    const promptTextarea = document.getElementById('prompt');
    const charCount = promptTextarea.value.length;
    const charCountDisplay = document.getElementById('charCount');
    
    charCountDisplay.textContent = `${charCount}/1000 characters`;
    
    if (charCount > 1000) {
        charCountDisplay.className = 'form-text text-danger';
    } else if (charCount > 800) {
        charCountDisplay.className = 'form-text text-warning';
    } else {
        charCountDisplay.className = 'form-text text-muted';
    }
}

async function handleGenerate(event) {
    event.preventDefault();
    
    const prompt = document.getElementById('prompt').value.trim();
    const style = document.getElementById('style').value;
    const ratio = document.getElementById('ratio').value;
    
    if (!prompt) {
        showError('Please enter a prompt for image generation.');
        return;
    }
    
    if (prompt.length > 1000) {
        showError('Prompt must be less than 1000 characters.');
        return;
    }
    
    // Show loading state
    showLoading();
    
    try {
        const params = new URLSearchParams({
            prompt: prompt,
            style: style,
            ratio: ratio
        });
        
        const response = await fetch(`/api/generate?${params}`);
        
        const data = await response.json();
        
        if (response.ok && data.success) {
            showSuccess(data);
        } else {
            showError(data.message || 'Failed to generate image');
        }
        
    } catch (error) {
        console.error('Error:', error);
        showError('Network error occurred. Please try again.');
    } finally {
        hideLoading();
    }
}

function showLoading() {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('errorAlert').style.display = 'none';
    document.getElementById('resultSection').style.display = 'none';
    document.getElementById('generateBtn').disabled = true;
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
    document.getElementById('generateBtn').disabled = false;
}

function showError(message) {
    document.getElementById('errorMessage').textContent = message;
    document.getElementById('errorAlert').style.display = 'block';
    document.getElementById('resultSection').style.display = 'none';
    hideLoading();
}

function showSuccess(data) {
    // Store image data for download
    currentImageData = data.image;
    
    // Display the generated image
    const imgElement = document.getElementById('generatedImage');
    imgElement.src = `data:image/png;base64,${data.image}`;
    imgElement.alt = `Generated image: ${data.prompt}`;
    
    // Show result section
    document.getElementById('errorAlert').style.display = 'none';
    document.getElementById('resultSection').style.display = 'block';
    
    hideLoading();
}

function downloadImage() {
    if (!currentImageData) {
        showError('No image available for download');
        return;
    }
    
    try {
        // Create download link
        const link = document.createElement('a');
        link.href = `data:image/png;base64,${currentImageData}`;
        link.download = `generated-image-${Date.now()}.png`;
        
        // Trigger download
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        
    } catch (error) {
        console.error('Download error:', error);
        showError('Failed to download image');
    }
}

// Health check function (optional)
async function checkHealth() {
    try {
        const response = await fetch('/api/health');
        const data = await response.json();
        console.log('API Health:', data);
    } catch (error) {
        console.error('Health check failed:', error);
    }
}

// Auto-resize textarea
document.getElementById('prompt').addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
});

// Sample prompts for inspiration
const samplePrompts = [
    "A serene mountain landscape at golden hour with a peaceful lake reflecting the sky",
    "A futuristic city skyline with flying cars and neon lights at night",
    "A magical forest with glowing mushrooms and fairy lights",
    "A cozy coffee shop interior with warm lighting and books on shelves",
    "A majestic dragon soaring through cloudy skies above ancient castle ruins",
    "An underwater scene with colorful coral reefs and tropical fish",
    "A steampunk airship floating above Victorian-era London",
    "A minimalist modern living room with natural light and plants"
];

// Add sample prompt functionality
function addSamplePromptButton() {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'btn btn-sm btn-outline-secondary mt-2';
    button.innerHTML = '<i class="fas fa-lightbulb"></i> Try a sample prompt';
    button.onclick = function() {
        const randomPrompt = samplePrompts[Math.floor(Math.random() * samplePrompts.length)];
        document.getElementById('prompt').value = randomPrompt;
        updateCharacterCount();
    };
    
    document.getElementById('prompt').parentNode.appendChild(button);
}

// Add sample prompt button after DOM is loaded
document.addEventListener('DOMContentLoaded', addSamplePromptButton);
