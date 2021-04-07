import nltk
import random
from nltk import LancasterStemmer
from numpy import array

from file_reader import read_intents_file
from preprocess import punctuation_removal

stemmer = LancasterStemmer()

intents = read_intents_file()

words = []
classes = []
documents = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # pattern = pattern.lower()
        pattern = punctuation_removal(pattern)
        # pattern = get_lemmatized_words(pattern)
        w = nltk.word_tokenize(pattern)
        words.extend(w)

        documents.append((w, intent['tag']))
        # add tags to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words]  # can be skipped if using lematization
words = sorted(list(set(words)))

# remove duplicate classes
classes = sorted(list(set(classes)))

print(len(documents), "documents", documents)
print(len(classes), "classes", classes)
print(len(words), " words", words)

training = []
output = []
# create an empty array for output
output_empty = [0] * len(classes)
print(output_empty)

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

for h in training:
    print(h)

random.shuffle(training)
training = array(training, dtype=object)

# creating training lists
features = list(training[:, 0])  # features
train_classes = list(training[:, 1])  # classes

print(len(features))

train_features = features[:(len(features) - 5)]
print(len(train_features))
test_features = features[-5:]
print(len(test_features))

print("\n\n")
print(train_features)
print(train_classes)
