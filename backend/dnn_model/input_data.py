import json
import nltk
import random
import string
from nltk import LancasterStemmer
from nltk.corpus import stopwords
from numpy import array

stemmer = LancasterStemmer()
stop_words = set(stopwords.words("english"))


def punctuation_removal(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def read_intents_file():
    filepath = 'corpus/intents.json'
    with open(filepath) as json_data:
        data = json.load(json_data)
    return data


intents = read_intents_file()

words = []
sentences = []
classes = []
documents = []


for intent in intents['intents']:
    for pattern in intent['patterns']:
        pattern = punctuation_removal(pattern)
        sentences.append(pattern)
        tokens = nltk.word_tokenize(pattern)
        word_tokens = [word for word in tokens]
        words.extend(word_tokens)
        documents.append((word_tokens, intent['tag']))
        # add tags to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

wordsWithoutStemming = [w.lower() for w in words]
words = [stemmer.stem(w.lower()) for w in words]  # can be skipped if using lematization
words = [w.lower() for w in words if w not in stop_words]
words = sorted(list(set(words)))

# remove duplicate classes
classes = sorted(list(set(classes)))

training = []
output = []
# create an empty array for output
output_empty = [0] * len(classes)

for doc in documents:
    bag_of_words = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    for w in words:
        bag_of_words.append(1) if w in pattern_words else bag_of_words.append(0)
    # output is '1' for current tag and '0' for rest of other tags
    # vectorizer for only individual word tokens wrt class.
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag_of_words, output_row])

random.shuffle(training)
training = array(training, dtype=object)

# creating training lists
features = list(training[:, 0])  # feature vectors
class_vec = list(training[:, 1])  # classes

# x_train = features[:(len(features) - 5)]
x_train, x_test = features, random.shuffle(features[:5])
y_train, y_test = class_vec, random.shuffle(class_vec[:2])