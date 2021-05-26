import nltk
from nltk.corpus import stopwords
from glove import embeddings
import time
import numpy as np
# import pickle

from file_reader import read_intents_file
from test_modules.preprocess import punctuation_removal

start = time.time()
intents = read_intents_file()
stop_words = set(stopwords.words("english"))

words = []
word_class_list = []
classes = []
print("hi3")
for intent in intents['intents']:
    tag = intent['tag']
    for pattern in intent['patterns']:
        pattern = punctuation_removal(pattern)
        pattern = pattern.lower()
        tokens = nltk.word_tokenize(pattern)
        words = [word for word in tokens if word not in stop_words]
        for t in words:
            temp_list = [t, tag]
            word_class_list.append(temp_list)
        if tag not in classes:
            classes.append(intent['tag'])

embedding = embeddings()

# gloveWordDictionary = open("data.pkl", "wb")
# pickle.dump(embedding, gloveWordDictionary)
# gloveWordDictionary.close()
# a_file = open("data.pkl", "rb")
# output = pickle.load(a_file)

training = []
for entry in word_class_list:
    temp = entry
    print(temp)
    word_embedding = embedding[temp[0]].tolist()
    print(word_embedding)
    class_embedding = embedding[temp[1]].tolist()
    print(class_embedding)
    t = [np.array(word_embedding), np.array(class_embedding)]
    training.append(t)

train_data = np.array(training)

x = []
y = []

xt = []
yt = []

for entry in train_data:
    temp = entry
    x.append(temp[0])
    y.append(temp[1])

print(len(x))
print(len(y))

xt = x[:5]
yt = y[:5]

print(len(xt))
print(len(yt))

print(classes)
end = time.time()
print("Time Taken : ", end - start)





