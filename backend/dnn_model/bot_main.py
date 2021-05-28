import tflearn
import random
import pymysql
import numpy as np
from nltk import LancasterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from input_data import x_train, y_train, classes, intents, words, punctuation_removal
# from memory_growth import memory_growth_exception
# from dnn_model import create_model

stop_words = set(stopwords.words("english"))
stemmer = LancasterStemmer()
connection = pymysql.connect(host="localhost", user="root", passwd="", database="chatbot")
cursor = connection.cursor()

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
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words if word not in stop_words]
    return sentence_words


def bag_of_words(sentence, word_set):
    sentence_words = input_sentence_words(sentence)
    bag = [0] * len(word_set)
    for s_words in sentence_words:
        for i, word in enumerate(word_set):
            if word == s_words:
                bag[i] = 1
    return np.array(bag)


def classify_query(sentence, threshold=0.25):
    results = model.predict([bag_of_words(sentence, words)])[0]
    results = [[i, r] for i, r in enumerate(results) if r > threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    return return_list


def getLeaveQuery(email, parameter):
    query = "select " + parameter + " from users u, leaves l where u.id=l.user_id and email='" + email + "'"
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
        return "You are not entitled to any " + parameter + " leaves. Please consult the person in charge."
    else:
        entry = str(row[0])
        return "You have " + entry + " " + parameter + " leave(s)."


def getSalaryQuery(email):
    query = "select salary, hra, allowance from users u, salary s where u.id=s.user_id and email='" + email + "'"
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
        response = "You are not entitled to any salary. Please consult the Accounts Department."
        return response
    else:
        response = "You salary is Rs. " + str(row[0]) + " \nHRA = Rs. " + str(row[1]) + " \nAllowance = Rs. " + str(row[2])
        return response


def bot_response(user_inputuery, email='gg@gmail.com'):
    response = ""
    classification = classify_query(user_inputuery)
    print(classification)
    print(classification[0][0])
    if len(classification) == 0:
        response = response + "Can you rephrase it?"
        return print(response)
    else:
        while classification:
            for i in intents['intents']:
                if i['tag'] == classification[0][0]:
                    parameter = 'sick'
                    if classification[0][0] == parameter:
                        response = getLeaveQuery(email, parameter)
                        return response
                    parameter = 'casual'
                    if classification[0][0] == parameter:
                        response = getLeaveQuery(email, parameter)
                        return response
                    parameter = 'salary'
                    if classification[0][0] == parameter:
                        response = getSalaryQuery(email)
                        return response
                    else:
                        # response = random.choice(i['responses'])
                        response = response + random.choice(i['responses'])
                        return response


while True:
    user_input = input("User: ")
    bot_r = bot_response(user_input)
    print("Bot: ", bot_r)
