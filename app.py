from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot
 
app = Flask(__name__)
bot = ChatBot()
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').strip()
    if not user_message:
        return jsonify({'response': 'Please say something!'})
    response = bot.get_response(user_message)
    return jsonify({'response': response})
 
if __name__ == '__main__':
    app.run(debug=True)
 