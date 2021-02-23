import string

import PyPDF2
import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# nltk.download('wordnet')

pdfFileObj = open('C:/Users/Muzaffar/Desktop/sample_corpus.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

totalPages = pdfReader.numPages
currentPageNumber = 0
text = ""

while currentPageNumber < totalPages:
    pageObj = pdfReader.getPage(0)
    text = text + pageObj.extractText()
    currentPageNumber += 1
# print(text)


sentTokens = sent_tokenize(text)
wordTokens = word_tokenize(text)
punctuations = ['(', ')', ';', ':', '[', ']', ',', '-', '.']
stopWords = stopwords.words('english')

keywordList = [word.lower() for word in wordTokens if not word in stopWords and not word in punctuations]

# print(keywordList.__len__())

# print(keywordList)

# pdfFileObj.close()

lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "namaste", "whats up", "good morning", "good afternoon", "good day")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


def request(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(user_response):
    bot_response = ''
    sentTokens.append(user_response)

    TfidfVectorObject = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVectorObject.fit_transform(sentTokens)
    values = cosine_similarity(tfidf[-1], tfidf)
    idx = values.argsort()[0][-2]
    flat = values.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        bot_response = bot_response + "I am sorry! I don't understand you"
        return bot_response
    else:
        bot_response = bot_response + sentTokens[idx]
        return bot_response


flag = True
print(
    "Chandler: Hello! I will answer your queries based on the document given to me. If you want to exit, type Bye")
while flag == True:
    user_response = input()
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response != 'thanks' and user_response != 'thank you':
            if request(user_response) is not None:
                print("Chandler: " + request(user_response))
            else:
                print("Chandler: ", end="")
                print(response(user_response))
                sentTokens.remove(user_response)
        else:
            flag = False
            print("Chandler: You are welcome..")
    else:
        flag = False
        print("Chandler: Bye! take care..")
