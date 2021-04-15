import nltk
import random
from nltk import LancasterStemmer
from numpy import array

from file_reader import read_intents_file
from preprocess import punctuation_removal
from sklearn.feature_extraction.text import TfidfVectorizer
from word_to_vec import word2vec_skipgrams

TfidfVectorizerObject = TfidfVectorizer()

stemmer = LancasterStemmer()

intents = read_intents_file()

words = []
sentences = []
classes = []
documents = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # pattern = pattern.lower()
        pattern = punctuation_removal(pattern)
        # pattern = get_lemmatized_words(pattern)
        sentences.append(pattern)
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

# --------------------------- TRAINING TESTING VECTOR SECTION START ---------------------

# print(len(documents), "documents", documents)
# print(len(classes), "classes", classes)
# print(len(words), " words", words)

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

# for h in training:
#     print(h)

random.shuffle(training)
training = array(training, dtype=object)

# creating training lists
features = list(training[:, 0])  # feature vectors
bog_train_classes = list(training[:, 1])  # classes

# print(len(features))

bog_train_features = features[:(len(features) - 5)]
bog_test_features = features[-5:]
# print(len(train_features))
# print(len(test_features))
#
# print("\n\n")
# print(train_features)
# print(train_classes)
#
# print(sentences)

# --------------------------- TRAINING TESTING VECTOR SECTION END ---------------------

# ------------------- Word2Vec Section -----------------------

word2vec_train_features = word2vec_skipgrams(words)
word2vec_class_vectors = word2vec_skipgrams(classes)


# print(feature_vectors)
# print(class_vectors)
#
# print(train_features)
# print(train_classes)


# ------------------- TFIDF SECTION --------------------------
# feature_vectors = TfidfVectorizerObject.fit_transform(words)
# print(feature_vectors)
# fArr = feature_vectors.toarray()
# for f in fArr:
#     print(f)
# class_vectors = TfidfVectorizerObject.fit_transform(classes)
# print(class_vectors)
# cArr = class_vectors.toarray()
# for c in cArr:
#     print(c)
# print(bog_train_features)
# print(word2vec_train_features)

print(word2vec_train_features)
print(word2vec_class_vectors)

