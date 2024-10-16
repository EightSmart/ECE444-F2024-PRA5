import flask
from flask import request, json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = flask.Flask(__name__)

@application.route('/')
def load_model():
    return "Welcome to ECE444 PRA5"

@application.route('/predict', methods=['POST', 'GET'])
def predict():
    data = request.json.get('news_string')

    loaded_model = None
    vectorizer = None

    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)
    
    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)

    prediction = loaded_model.predict(vectorizer.transform([data]))[0]
    return prediction


if __name__ == '__main__':
   application.run()

