from random import random

from nltk import LancasterStemmer, word_tokenize

from memory_growth import memory_growth_exception
from model import create_model
from input_data import train_features, train_classes, features, words, intents, classes, feature_vectors, class_vectors
from preprocess import punctuation_removal
from numpy import array

stemmer = LancasterStemmer()

memory_growth_exception()

model = create_model(feature_vectors, class_vectors)


def input_sentence_words(sentence):
    sentence = punctuation_removal(sentence)
    sentence_words = word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence, word_set):
    sentence_words = input_sentence_words(sentence)
    bag = [0] * len(word_set)
    for s_words in sentence_words:
        for i, words in enumerate(word_set):
            if words == s_words:
                bag[i] = 1
    # print(array(bag))
    # print(word_set)
    return array(bag)


threshold = 0.30


def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bag_of_words(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i, r] for i, r in enumerate(results) if r > threshold]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of class and probability
    # print(results)
    # print(return_list)
    return return_list


print(feature_vectors)
print(class_vectors)

i = 0

while i < 20:
    g = input()
    classify(g)
    i = i + 1
