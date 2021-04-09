import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

import tensorflow as tf

with open('uwu_intents.json') as file:
    intents_json = json.load(file)  
    try:
        with open('data.pickle', 'rb') as f:
            words, labels = pickle.load(f)
        model = tf.keras.models.load_model('UwUchat.h5')
    except:
        print("oopsie, I'm missing data, please train me :3")


def clean_sentence(sentence):
    """
    Input: string
    Output: list of lemmatized words
    """
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [ lemmatizer.lemmatize(word) for word in sentence_words ]
    return sentence_words

def bag_of_words(sentence):
    """
    Input: string
    Output: numpy array 
    """
    sentence_words = clean_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_intent(sentence):
    bag = bag_of_words(sentence)
    res = model.predict(np.array([bag]))[0]
    ERR_THRESHOLD = 0.25 # any results less certain than this get thrown out
    results = [ [i, r] for i, r in enumerate(res) if r > ERR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True) # sorts list, but we only use the highest one? can we use max?
    return_list = []
    for r in results:
        return_list.append({'intent':labels[r[0]], 'probability':str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    for i in intents_json['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses'])
    return "I don't know what to say :(" # this will be returned if the model did not identify an intent


def converse(message):
    ints = predict_intent(message)
    res = get_response(ints, intents_json)
    return "UwU: " + res


if __name__ == "__main__":
    while True:
        message = input("You: ")
        if message == 'quit':
            break
        print(converse(message))
