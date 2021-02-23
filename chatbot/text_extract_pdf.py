import PyPDF2
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def getSentTokens(filename):
    pdfFileObj = open(filename, 'rb')
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
    #wordTokens = word_tokenize(text)

    return sentTokens
