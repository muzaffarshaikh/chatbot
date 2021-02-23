# Extracts keywords from PDF but the keywords are irregular
# find another way to split
# https://www.dev2qa.com/how-to-extract-text-from-pdf-in-python/

import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def extractPdfText(filePath=''):
    fileObject = open(filePath, 'rb')
    pdfFileReader = PyPDF2.PdfFileReader(fileObject)
    totalPageNumber = pdfFileReader.numPages
    print('This pdf file contains totally ' + str(totalPageNumber) + ' pages.')
    currentPageNumber = 0
    text = ''

    while currentPageNumber < totalPageNumber:
        pdfPage = pdfFileReader.getPage(currentPageNumber)
        text = text + pdfPage.extractText()
        currentPageNumber += 1

    if text == '':
        text = textract.process(filePath, method='tesseract', encoding='utf-8')

    return text


def extractKeywords(text):
    wordTokens = word_tokenize(text)
    punctuations = ['(', ')', ';', ':', '[', ']', ',']
    stopWords = stopwords.words('english')
    keywordList = [word for word in wordTokens if not word in stopWords and not word in punctuations]
    return keywordList


if __name__ == '__main__':
    pdfFilePath = 'C:/Users/Muzaffar/Desktop/ss.pdf'
    pdfText = extractPdfText(pdfFilePath)
    print('There are ' + str(pdfText.__len__()) + ' word in the pdf file.')
    keywords = extractKeywords(pdfText)
    print('There are ' + str(keywords.__len__()) + ' keyword in the pdf file.')
    print(pdfText)
