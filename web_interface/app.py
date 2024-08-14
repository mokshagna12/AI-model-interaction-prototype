# web_interface/app.py
from flask import Flask, request, jsonify
from chatbot.basic_chatbot import chatbot
from text_to_image.generate_image import generate_image

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Process user_input with chatbot and generate response
    response = chatbot_response(user_input)
    return jsonify({'response': response})

@app.route('/generate-image', methods=['POST'])
def generate_image_route():
    prompt = request.json.get('prompt')
    image_url = generate_image(prompt)
    return jsonify({'image_url': image_url})

def chatbot_response(user_input):
    # Implement chatbot response logic
    return "This is a placeholder response."

if __name__ == "__main__":
    app.run(debug=True)
 
