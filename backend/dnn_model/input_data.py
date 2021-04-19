import nltk
import random
from nltk import LancasterStemmer
from nltk.corpus import stopwords
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

stop_words = set(stopwords.words("english"))
print(stop_words)

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # pattern = pattern.lower()
        pattern = punctuation_removal(pattern)
        # pattern = get_lemmatized_words(pattern)
        sentences.append(pattern)
        tokens = nltk.word_tokenize(pattern)
        print(tokens)
        word_tokens = [word for word in tokens if word not in stop_words]
        print(word_tokens)
        words.extend(word_tokens)
        documents.append((word_tokens, intent['tag']))
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

random.shuffle(training)
training = array(training, dtype=object)

print(training)

# creating training lists
features = list(training[:, 0])  # feature vectors
y_train = list(training[:, 1])  # classes
y_test = y_train

print(len(features))
print(len(y_train))

# print(len(features))

x_train = features[:(len(features) - 5)]
x_test = x_train
# print(len(train_features))
# print(len(test_features))
#
# print("\n\n")
# print(train_features)
print(type(x_train[0]))
print(len(x_train[0]))
# print(train_classes)
#
# print(sentences)

for h in x_train:
    print(h)

for l in y_train:
    print(l)
# --------------------------- TRAINING TESTING VECTOR SECTION END ---------------------

# ------------------- Word2Vec Section -----------------------

# word2vec_train_features = word2vec_skipgrams(words)
# word2vec_class_vectors = word2vec_skipgrams(classes)

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

# print(word2vec_train_features)
# print(word2vec_class_vectors)
