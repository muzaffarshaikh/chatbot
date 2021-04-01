import nltk
from nltk import LancasterStemmer

import numpy as np

from memory_growth import memory_growth_exception
from preprocess import punctuation_removal
from model import create_model
from input_data import train_features, train_classes, test_features, features, words
from user_input import input_sentence_words, bag_of_words_user_query

stemmer = LancasterStemmer()

memory_growth_exception()

model = create_model(features, train_classes)

# model.save('model.tflearn')
# model.load('./model.tflearn')

temp_train_classes = []

for t in train_classes:
    temp_train_vector = np.pad(t, (0, 52), 'constant')
    temp_train_classes.append(temp_train_vector)


# Evaluate model
score = model.evaluate(test_features, temp_train_classes)
print(score)
#
# predictions = model.predict(test_features)
# predictions = np.array([np.argmax(pred) for pred in predictions])
# train_classes = np.array([np.argmax(each) for each in train_classes])
#
# acc = 100 * np.sum(predictions == train_classes) / len(train_classes)
#
# print(acc)

# Run the model on one example
prediction = model.predict()
print(prediction)

# user_sentence = input_sentence_words(input())

# bog_array = bag_of_words_user_query(user_sentence, words)

# print(bog_array)
