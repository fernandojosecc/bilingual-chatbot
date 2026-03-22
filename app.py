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
            return jsonify({'error': 'No message provided'}), 400
        
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
        
        return jsonify({'response': ai_response})
        
    except Exception as e:
        return jsonify({'error': f'Something went wrong: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
