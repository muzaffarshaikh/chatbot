from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# remove stopwords function
def get_tokenize_text(text):
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text)
    word_tokens = [word for word in tokens if word not in stop_words]
    return word_tokens
