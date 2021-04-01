import nltk
from nltk import LancasterStemmer

import numpy as np

from memory_growth import memory_growth_exception
from preprocess import punctuation_removal
from model import create_model
from input_data import train_features, train_classes, test_features, features

stemmer = LancasterStemmer()

memory_growth_exception()

model = create_model(features, train_classes)

# model.save('model.tflearn')
# model.load('./model.tflearn')


# Evaluate model
# score = model.evaluate(test_features, train_classes)
# print(score)
#
# predictions = model.predict(test_features)
# predictions = np.array([np.argmax(pred) for pred in predictions])
# train_classes = np.array([np.argmax(each) for each in train_classes])
#
# acc = 100 * np.sum(predictions == train_classes) / len(train_classes)
#
# print(acc)

# Run the model on one example
# prediction = model.predict()
# print(prediction)


def input_sentence(sentence):
    # tokenizing the pattern
    sentence = punctuation_removal(sentence)
    sentence_words = nltk.word_tokenize(sentence)
    # stemming each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words
