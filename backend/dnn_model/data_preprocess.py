import string
import inflect
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
import nltk

# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')

p = inflect.engine()
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


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


def punctuation_removal(text):

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
    tag = pos_tag([token])[0][1][0].upper()
    return tag_dict.get(tag, wordnet.NOUN)


def get_lemmatized_words(string_data):
    token_list = string_data.split()
    lemmatized_output_with_POS_information = [lemmatizer.lemmatize(token, get_part_of_speech_tags(token)) for token in
                                              token_list]
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


def preprocess(text):
    t1 = punctuation_removal(text)
    t2 = get_lemmatized_words(t1)
    return t2

# def pre_process_data(corpus, number_conversion, remove_punctuation, stemming, lemmatization):
#
#     if number_conversion:
#         corpus = convert_number_to_word(corpus)
#
#     if remove_punctuation:
#         corpus = remove_punctuation(corpus)
#
#     if stemming:
#         corpus = get_stemmed_words(corpus)
#
#     if lemmatization:
#         corpus = get_lemmatized_words(corpus)
#
#
#     return corpus
