import nltk
import random
from nltk import LancasterStemmer
from nltk.corpus import stopwords
from numpy import array

from file_reader import read_intents_file
from data_preprocess import punctuation_removal

stemmer = LancasterStemmer()
intents = read_intents_file()

words = []
sentences = []
classes = []
documents = []

stop_words = set(stopwords.words("english"))
print(stop_words)

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # pattern = pattern.lower()
        pattern = punctuation_removal(pattern)
        # pattern = get_lemmatized_words(pattern)
        sentences.append(pattern)
        tokens = nltk.word_tokenize(pattern)
        word_tokens = [word for word in tokens if word not in stop_words]
        words.extend(word_tokens)
        documents.append((word_tokens, intent['tag']))
        # add tags to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words]  # can be skipped if using lematization
words = sorted(list(set(words)))

# remove duplicate classes
classes = sorted(list(set(classes)))

training = []
output = []
# create an empty array for output
output_empty = [0] * len(classes)
# print(output_empty)

for doc in documents:
    # initialize bag_of_words of words
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

