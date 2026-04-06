import json
import random
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os
 
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)
 
lemmatizer = WordNetLemmatizer()
 
class ChatBot:
    def __init__(self, intents_file='intents.json'):
        self.intents_file = intents_file
        self.intents = []
        self.vectorizer = TfidfVectorizer(tokenizer=self.tokenize, lowercase=True)
        self.classifier = LogisticRegression(max_iter=1000, random_state=42)
        self.trained = False
        self.load_and_train()
 
    def tokenize(self, text):
        tokens = nltk.word_tokenize(text.lower())
        return [lemmatizer.lemmatize(t) for t in tokens if t.isalpha()]
 
    def load_and_train(self):
        with open(self.intents_file, 'r') as f:
            data = json.load(f)
        self.intents = data['intents']
 
        training_sentences = []
        training_labels = []
 
        for intent in self.intents:
            if intent['tag'] == 'unknown':
                continue
            for pattern in intent['patterns']:
                training_sentences.append(pattern)
                training_labels.append(intent['tag'])
 
        if not training_sentences:
            return
 
        X = self.vectorizer.fit_transform(training_sentences)
        self.classifier.fit(X, training_labels)
        self.trained = True
 
    def predict_intent(self, text):
        if not self.trained:
            return 'unknown'
        X = self.vectorizer.transform([text])
        proba = self.classifier.predict_proba(X)[0]
        max_proba = max(proba)
        if max_proba < 0.25:
            return 'unknown'
        return self.classifier.predict(X)[0]
 
    def get_response(self, text):
        tag = self.predict_intent(text)
        for intent in self.intents:
            if intent['tag'] == tag:
                return random.choice(intent['responses'])
        return "I'm not sure how to respond to that. Try asking something else!"
 