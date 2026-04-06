AI Powered Chatbot
An intelligent chatbot built with Python, NLTK, and Scikit-learn. Uses Natural Language Processing (NLP) to understand user input and a Logistic Regression classifier to predict intent. Served through a Flask web interface.
Features

Intent classification using TF-IDF + Logistic Regression
NLP preprocessing with NLTK (tokenization + lemmatization)
Clean, modern chat UI built with HTML/CSS/JS
Easy to extend with new intents in intents.json

Tech Stack

Python — core language
NLTK — tokenization and lemmatization
Scikit-learn — TF-IDF vectorizer + Logistic Regression classifier
Flask — web server
HTML/CSS/JS — frontend chat interface

Project Structure
ai-chatbot/
├── app.py              # Flask server
├── chatbot.py          # NLP + ML logic
├── intents.json        # Training data (patterns and responses)
├── requirements.txt    # Python dependencies
└── templates/
    └── index.html      # Chat UI
Setup & Run

Clone the repository:

bashgit clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot

Install dependencies:

bashpip install -r requirements.txt

Run the app:

bashpython app.py

Open your browser and go to:

http://localhost:5000
How It Works

User types a message in the chat UI
The message is sent to the Flask backend via a POST request
chatbot.py tokenizes and lemmatizes the text using NLTK
TF-IDF vectorizer converts the text to numerical features
Logistic Regression predicts the intent (e.g., greeting, joke, help)
A random response is selected from the matched intent and returned

Author
Muhammed Adhil M J — B.Tech AI & ML, Vidya Academy of Science and Technology
