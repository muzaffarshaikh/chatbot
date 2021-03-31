import nltk
from nltk import LancasterStemmer

from memory_growth import memory_growth_exception
from preprocess import punctuation_removal
from model import create_model
from input_data import train_features, train_classes


stemmer = LancasterStemmer()

memory_growth_exception()

model = create_model(train_features, train_classes)

# model.save('model.tflearn')
# model.load('./model.tflearn')


# Evaluate model
score = model.evaluate()
print(score)

# Run the model on one example
prediction = model.predict()
print(prediction)


def input_sentence(sentence):
    # tokenizing the pattern
    sentence = punctuation_removal(sentence)
    sentence_words = nltk.word_tokenize(sentence)
    # stemming each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words
