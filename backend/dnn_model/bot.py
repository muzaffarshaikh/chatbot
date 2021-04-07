from random import random

from nltk import LancasterStemmer, word_tokenize

from memory_growth import memory_growth_exception
from model import create_model
from input_data import train_features, train_classes, test_features, features, words, intents, classes
from preprocess import punctuation_removal
from numpy import array

stemmer = LancasterStemmer()

memory_growth_exception()

model = create_model(features, train_classes)


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
    return array(bag)


error_threshold = 0.30


def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bag_of_words(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i, r] for i, r in enumerate(results) if r > error_threshold]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((train_classes[r[0]], r[1]))
    # return tuple of intent and probability
    print(return_list)
    return return_list


def response(sentence):
    results = classify(sentence)
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # a random response from the intent
                    return print(random.choice(i['responses']))
            results.pop(0)



classify('what are my sick leaves?')
