import tflearn
from nltk import LancasterStemmer

from memory_growth import memory_growth_exception
from dnn_model import create_model
from input_data import x_train, y_train, classes, intents, words
import random
from data_preprocess import punctuation_removal
import numpy as np
from nltk.tokenize import word_tokenize

import pymysql

connection = pymysql.connect(host="localhost", user="root", passwd="", database="chatbot")
cursor = connection.cursor()

memory_growth_exception()
stemmer = LancasterStemmer()

# model = create_model(x_train, y_train)
# model.save('model.tflearn')

network_layers = tflearn.input_data(shape=[None, len(x_train[0])])
network_layers = tflearn.fully_connected(network_layers, 10)
network_layers = tflearn.fully_connected(network_layers, 10)
network_layers = tflearn.fully_connected(network_layers, len(y_train[0]), activation='softmax')
network_layers = tflearn.regression(network_layers, optimizer='adam')
model = tflearn.DNN(network_layers)
model.load('./model.tflearn')


def input_sentence_words(sentence):
    sentence = punctuation_removal(sentence)
    sentence_words = word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence, word_set):
    sentence_words = input_sentence_words(sentence)
    bag = [0] * len(word_set)
    for s_words in sentence_words:
        for i, wordz in enumerate(word_set):
            if wordz == s_words:
                bag[i] = 1
    return np.array(bag)


threshold = 0.25


def classify_query(sentence):
    results = model.predict([bag_of_words(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i, r] for i, r in enumerate(results) if r > threshold]
    # sort by probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    return return_list


def getLeaveQuery(username, parameter):
    query = "select " + parameter + " from users u, leaves l where u.id=l.user_id and username='" + username + "'"
    cursor.execute(query)
    row = cursor.fetchone()
    entry = str(row[0])
    return entry


def getSalaryQuery(username):
    query = "select salary, hra, allowance from users u, salary s where u.id=s.user_id and username='" + username + "'"
    cursor.execute(query)
    row = cursor.fetchone()
    entry = list(row)
    return entry


def bot_response(user_query, username='mzfrxec'):
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
                    parameter = 'sick'
                    if classification[0][0] == parameter:
                        sick_leave = getLeaveQuery(username, parameter)
                        response = "You have " + sick_leave + " sick leave(s)."
                        return response
                    parameter = 'casual'
                    if classification[0][0] == parameter:
                        casual_leave = getLeaveQuery(username, parameter)
                        response = "You have " + casual_leave + " casual leave(s)."
                        return response
                    parameter = 'salary'
                    if classification[0][0] == parameter:
                        salary = getSalaryQuery(username)
                        if salary[0] == 0:
                            response = "You are not entitled to any salary"
                        else:
                            response = "You salary is Rs. " + str(salary[0]) + " \nHRA = Rs. " + str(salary[1]) + " \nHRA = Rs. " + str(salary[2])
                        return response
                    else:
                        # response = random.choice(i['responses'])
                        response = response + random.choice(i['responses'])
                        return response


while True:
    user_q = input("User: ")
    bot_r = bot_response(user_q)
    print("Bot: ", bot_r)
