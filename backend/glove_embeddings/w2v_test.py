# Glove Cosine Test

import numpy as np
from nltk.corpus import stopwords
from test_modules.preprocess import punctuation_removal
from glove import embeddings

#
embedding_dict = {}
embedding_dict = embeddings()

stop_words = set(stopwords.words("english"))

documents = ['Machine learning is the study of computer algorithms that improve automatically through experience.',
             'Machine learning algorithms build a mathematical model based on sample data, known as training data. ',
             'The discipline of machine learning employs various approaches to teach computers to accomplish tasks where no fully satisfactory algorithm is available.',
             'Machine learning is closely related to computational statistics, which focuses on making predictions using computers.',
             'The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning.',
             'Machine learning involves computers discovering how they can perform tasks without being explicitly programmed to do so.',
             'It involves computers learning from data provided so that they carry out certain tasks.',
             'Machine learning approaches are traditionally divided into three broad categories, depending on the nature of the "signal" or "feedback" available to the learning system: Supervised, Unsupervised and Reinforcement',
             'Software engineering is the systematic application of engineering approaches to the development of software.',
             'Software engineering is a computing discipline.',
             'A software engineer creates programs based on logic for the computer to execute.',
             'A software engineer has to be more concerned about the correctness of the program in all the cases. Meanwhile, a data scientist is comfortable with uncertainty and variability.',
             'Developing a machine learning application is more iterative and explorative process than software engineering.'
             ]

sentences = []

for document in documents:
    temp_doc = document.lower()
    temp_doc = punctuation_removal(temp_doc)
    sentences.append(temp_doc)

doc2vec = []
# word2vec_dict = {}

for sentence in sentences:
    cp = sentence
    words = sentence.split(" ")
    sent_embedding = []
    for word in words:

        try:
            w_embedding = np.array(embedding_dict[word])
            w_embedding.resize(5)
            for w in w_embedding:
                sent_embedding.append(w)
        except:
            print("wrong")

    print(len(sent_embedding), cp, sent_embedding)

#        word2vec_dict[w_embedding] = word

#         for w in w_embedding:
#             s_vector = []
#             s_vector.append(w)
#             sent_vector = np.array(s_vector)
#             doc2vec.append(sent_vector)
#
# print(doc2vec)
#print(word2vec_dict)