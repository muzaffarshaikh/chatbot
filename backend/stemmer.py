from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()


def get_stemmed_words(word_tokens):
    stems = [stemmer.stem(word) for word in word_tokens]
    return stems
