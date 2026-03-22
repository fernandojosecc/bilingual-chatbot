from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# System prompt for bilingual responses
SYSTEM_PROMPT = """You are a helpful bilingual assistant. Always respond in both English and Spanish.
Format your response with 'English:' first, then 'Español:' below it."""

@app.route('/')
def index():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages and get AI response"""
    try:
        user_message = request.json.get('message', '')
        
        if not user_message:
            return jsonify({
                'error': 'Please enter a message before sending.',
                'error_type': 'validation'
            }), 400
        
        # Check if OpenAI API key is configured
        if not openai.api_key:
            return jsonify({
                'error': 'OpenAI API key is not configured. Please check your .env file.',
                'error_type': 'configuration'
            }), 500
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        if not ai_response:
            return jsonify({
                'error': 'The AI assistant returned an empty response. Please try again.',
                'error_type': 'api'
            }), 500
        
        return jsonify({'response': ai_response})
        
    except openai.error.RateLimitError:
        return jsonify({
            'error': 'The AI service is experiencing high demand. Please wait a moment and try again.',
            'error_type': 'rate_limit'
        }), 429
        
    except openai.error.AuthenticationError:
        return jsonify({
            'error': 'There\'s an issue with the API key. Please check your configuration.',
            'error_type': 'authentication'
        }), 401
        
    except openai.error.APIError as e:
        return jsonify({
            'error': 'The AI service encountered an error. Please try again.',
            'error_type': 'api',
            'details': str(e)
        }), 500
        
    except openai.error.Timeout:
        return jsonify({
            'error': 'The request timed out. The AI might be taking too long to respond. Please try again.',
            'error_type': 'timeout'
        }), 408
        
    except Exception as e:
        return jsonify({
            'error': 'An unexpected error occurred. Please try again or contact support if the problem persists.',
            'error_type': 'unknown',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
