from nltk import LancasterStemmer

from memory_growth import memory_growth_exception
from dnn_model import create_model
from input_data import x_train, y_train, classes, intents, words
import random
from data_preprocess import punctuation_removal
import numpy as np
from nltk.tokenize import word_tokenize

memory_growth_exception()
stemmer = LancasterStemmer()

model = create_model(x_train, y_train)


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
    return np.array(bag)


threshold = 0.25


def classify_query(sentence):
    results = model.predict([bag_of_words(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i, r] for i, r in enumerate(results) if r > threshold]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # list of class and probability
    return return_list


def bot_response(user_query, USERNAME='mzfrxec'):
    response = ""
    classification = classify_query(user_query)
    print(classification)
    print(classification[0][0])
    if len(classification) == 0:
        response = response + "Can you repharse it?"
        return print(response)
    else:
        while classification:
            for i in intents['intents']:
                if i['tag'] == classification[0][0]:
                    # response = random.choice(i['responses'])
                    response = response + random.choice(i['responses'])
                    return response


while True:
    user_q = input("User: ")
    bot_r = bot_response(user_q)
    print("Bot: ", bot_r)
