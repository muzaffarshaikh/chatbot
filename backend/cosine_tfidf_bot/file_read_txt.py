from nltk import sent_tokenize
from nltk.corpus import stopwords

filename = 'data/corpus.txt'

with open(filename, 'r') as file:
    data = file.read().replace('\n', '')
    file.close()

    data.lower()
    stop_words = set(stopwords.words("english"))
    tokens = sent_tokenize(data)
    sent_tokens = [word for word in tokens if word not in stop_words]

print(sent_tokens)