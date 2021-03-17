import inflect
import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag

# nltk.download('averaged_perceptron_tagger')

from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

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


def get_part_of_speech_tags(token):
    tag_dict = {
        "J": wordnet.ADJ,
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "R": wordnet.ADV
    }
    tag = nltk.pos_tag([token])[0][1][0].upper()
    return tag_dict.get(tag, wordnet.NOUN)


def get_lemmatized_words(string_data):
    token_list = string_data.split()
    lemmatized_output_with_POS_information = [lemmatizer.lemmatize(token, get_part_of_speech_tags(token)) for token in token_list]
    lemmatized_op = ' '.join(lemmatized_output_with_POS_information)
    return lemmatized_op


# remove stopwords function
def get_tokenized_words(text):
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text)
    word_tokens = [word for word in tokens if word not in stop_words]
    return word_tokens


def get_tokenized_sentences(text):
    stop_words = set(stopwords.words("english"))
    tokens = sent_tokenize(text)
    sent_tokens = [word for word in tokens if word not in stop_words]
    return sent_tokens
