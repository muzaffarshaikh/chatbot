# chatbot-python-test

Reference: https://medium.com/analytics-vidhya/building-a-simple-chatbot-in-python-using-nltk-7c8c8215ac6e

A text retrieval chatbot.
Uses nltk and sklearn python libraries.
Based on TFIDF Scoring and Cosine Similarity.

Issue 1: While extracting data from PDFs downloaded from internet, couldn't extract keywords even though the PDF contains text. The data comes as special characters. So, created a sample pdf. (data/sample_corpus.pdf). Can extract text tokens from the self created PDF.

Issue 2: Sentence token extraction needs to be handled properly so that proper sentences are scored and retrieved.

