import nltk
from nltk.corpus import stopwords
from glove import load_embeddings_dict

from file_reader import read_intents_file
from preprocess import punctuation_removal

intents = read_intents_file()
stop_words = set(stopwords.words("english"))

words = []
word_class_list = []

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

print(word_class_list)
embeddings = load_embeddings_dict()
training = []
for entry in word_class_list:
    temp = entry
    word_embedding = embeddings[temp[0]].tolist()
    class_embedding = embeddings[temp[1]].tolist()
    t = [word_embedding, class_embedding]
    training.append(t)

x_train = []
y_train = []

for entry in training:
    temp = entry
    x_train.append(temp[0])
    y_train.append(temp[1])

print(x_train)
print(y_train)






