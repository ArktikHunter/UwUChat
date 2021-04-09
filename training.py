import numpy as np
import random
import pickle

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

import json
with open('uwu_intents.json') as file:
    data = json.load(file)  # loads all the data into a dictionary 


words = []
labels = []
docs = []
ignore_letters = ['.', ',', '!'] 

for intent in data['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)                     # adds new words to word list
        docs.append((word_list, intent['tag']))     # adds link between current words and tag for training

        if intent['tag'] not in labels:
            labels.append(intent['tag'])


words = [ lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters ]
words = sorted(set(words)) # eliminates duplicates

with open('data.pickle', 'wb') as f:
	pickle.dump((words, labels), f)

training = []
output_empty = [0] * len(labels)

for doc in docs:
    bag = []
    word_patterns = doc[0]
    word_patterns = [ lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[labels.index(doc[1])] = 1 # what?
    training.append([bag, output_row])

training = np.array(training)


# the model will be trained to match the list of words (train_x) to the correct intent label (train_y)
train_x = list(training[:, 0])
train_y = list(training[:, 1])


model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('UwUchat.h5')

print("Done :3")
