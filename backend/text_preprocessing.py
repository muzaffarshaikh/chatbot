import inflect
import string
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
p = inflect.engine()


def convert_number_to_word(text):
    temp_str = text.split()
    new_string = []

    for word in temp_str:
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)
        else:
            new_string.append(word)

    temp_str = ' '.join(new_string)
    return temp_str


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def get_stemmed_words(word_tokens):
    stems = [stemmer.stem(word) for word in word_tokens]
    return stems


# remove stopwords function
def get_tokenized_text(text):
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text)
    word_tokens = [word for word in tokens if word not in stop_words]
    return word_tokens
