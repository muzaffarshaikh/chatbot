from nltk import LancasterStemmer

from memory_growth import memory_growth_exception
from dnn_model import create_model
from input_data import x_train, y_train, classes, intents, words
import random
from data_preprocess import punctuation_removal
from numpy import array
from nltk.tokenize import word_tokenize

memory_growth_exception()
stemmer = LancasterStemmer()

model = create_model(x_train, y_train)


# print("Input sentence : ")
# g = input().lower()
# g_p = punctuation_removal(g)
# arr = g_p.split(" ")
# sent_vector = []
# for l in arr:
#     temp = embedding[l]
#     sent_vector.append(temp)
# for j in sent_vector:
#     print(j)
# results = model.predict([sent_vector[0]])[0]
# results = [[i, r] for i, r in enumerate(results)]
# print(results)
# results = [[i, r] for i, r in enumerate(results)]
# print(results)
# #
# # x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=1)
# # x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=1)
# #
# # model.fit(x_train, y_train, validation_set=(x_test, y_test), n_epoch=10, show_metric=True, batch_size=64,
# #           snapshot_step=1, snapshot_epoch=True, run_id='name_model')
# #
# # graph = tf.Graph()
# # with graph.as_default():
# #     net = tflearn.input_data([None, 2])
# #     net = tflearn.fully_connected(net, 6, activation='tanh', weights_init='normal')
# #
# # sess = tf.Session(graph=graph)
# # writer = tf.train.SummaryWriter('tmp/tensorboard_log', sess.graph)
#
#
# # loss_train = history.history['train_loss']
# # loss_val = history.history['val_loss']
# # epochs = range(1,35)
# # plt.plot(epochs, loss_train, 'g', label='Training loss')
# # plt.plot(epochs, loss_val, 'b', label='validation loss')
# # plt.title('Training and Validation loss')
# # plt.xlabel('Epochs')
# # plt.ylabel('Loss')
# # plt.legend()
# # plt.show()
#
#
def input_sentence_words(sentence):
    sentence = punctuation_removal(sentence)
    sentence_words = word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words


#
#
# # def get_glove_vector(sentence, word_set):
# #     sentence_words = input_sentence_words(sentence)
#
#
def bag_of_words(sentence, word_set):
    sentence_words = input_sentence_words(sentence)
    bag = [0] * len(word_set)
    for s_words in sentence_words:
        for i, words in enumerate(word_set):
            if words == s_words:
                bag[i] = 1
    print(array(bag))
    # print(word_set)
    return array(bag)


threshold = 0.50


def classify_query(sentence):
    results = model.predict([bag_of_words(sentence, words)])[0]
    print(results)
    # filter out predictions below a threshold
    results = [[i, r] for i, r in enumerate(results) if r > threshold]
    # sort by strength of probability
    print(results)
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of class and probability
    print(return_list)
    return return_list


def bot_response(user_query):
    classification = classify_query(user_query)
    if len(classification) == 0:
        print("Can you repharse it?")
    else:
        while classification:
            for i in intents['intents']:
                if i['tag'] == classification[0][0]:
                    # response = random.choice(i['responses'])
                    return print(random.choice(i['responses']))


while True:
    g = input()
    bot_response(g)
