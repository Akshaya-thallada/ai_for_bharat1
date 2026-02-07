"""
BharatSaarthi Web Application
Flask-based web interface for hackathon demo
"""

from flask import Flask, render_template, request, jsonify
import sys
sys.path.append('src')

from nlp.intent_classifier import IntentClassifier
from core.ai_engine import BharatSaarthiEngine

app = Flask(__name__)

# Initialize AI components
classifier = IntentClassifier()
engine = BharatSaarthiEngine()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Process the message
    intent = classifier.classify(user_message)
    response = engine.process(user_message, intent)
    
    return jsonify({
        'intent': intent,
        'response': response
    })

if __name__ == '__main__':
    print("🇮🇳 BharatSaarthi Web App Starting...")
    print("=" * 50)
    print("✓ AI Engine loaded")
    print("✓ Web server starting...")
    print("\n🌐 Open your browser and go to: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
