# 🤖 Bilingual Chatbot

A sophisticated AI-powered chatbot that responds in both English and Spanish, built with Flask and OpenAI's GPT-3.5-turbo model. This project demonstrates modern web development, API integration, and bilingual AI capabilities.

## 🌟 Live Demo

**[Try the live chatbot here](https://your-railway-app-url.railway.app)**

## ✨ Features

- **Bilingual Responses**: Every AI response is provided in both English and Spanish
- **Modern UI**: Clean, professional chat interface inspired by popular messaging apps
- **Error Handling**: Comprehensive error handling with retry functionality
- **Mobile Responsive**: Works seamlessly on desktop and mobile devices
- **Production Ready**: Deployed on Railway with proper configuration

## 🛠 Tech Stack

- **Backend**: Python 3.9+, Flask
- **AI Model**: OpenAI GPT-3.5-turbo API
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Deployment**: Railway.app
- **Environment Management**: python-dotenv
- **Production Server**: Gunicorn

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/bilingual-chatbot.git
   cd bilingual-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
bilingual-chatbot/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Chat interface
├── requirements.txt       # Python dependencies
├── Procfile              # Railway deployment configuration
├── .env                  # Environment variables (not in git)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🎯 How It Works

1. **User Input**: Messages are sent through the web interface
2. **API Integration**: Flask backend forwards messages to OpenAI's API
3. **Bilingual Processing**: System prompt ensures responses in both languages
4. **Display**: Responses are parsed and displayed with proper formatting
5. **Error Handling**: Comprehensive error handling with retry options

## 🔧 Configuration

The chatbot uses a custom system prompt to ensure bilingual responses:

```
You are a helpful bilingual assistant. Always respond in both English and Spanish.
Format your response with 'English:' first, then 'Español:' below it.
```

## 🚀 Deployment

This app is optimized for Railway.app deployment:

- **Procfile** included for web process configuration
- **Environment variables** for API keys
- **Production-ready** Flask configuration
- **Gunicorn** as production WSGI server

## 🧪 Testing

### Local Testing
```bash
# Run the app locally
python app.py

# Test with curl
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, how are you?"}'
```

### Production Testing Checklist
- ✅ Verify API key is properly configured
- ✅ Test bilingual responses
- ✅ Check error handling for invalid inputs
- ✅ Test mobile responsiveness
- ✅ Verify retry functionality

## 🤝 Contributing

This project is part of my AI engineering portfolio. Feel free to explore the code and provide feedback!

## 👨‍💻 About the Developer

**Fernando Contreras** - AI Tools Specialist

This project was built as part of my AI engineering portfolio to demonstrate:
- Full-stack web development skills
- AI API integration
- Bilingual application development
- Modern UI/UX design
- Production deployment practices

## 📧 Contact

- **Portfolio**: [your-portfolio-url]
- **LinkedIn**: [your-linkedin-url]
- **GitHub**: [your-github-url]

---

⭐ **Built with ❤️ and AI**