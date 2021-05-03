import pickle
import numpy as np
import time
from preprocess import punctuation_removal

from cosine_tfidf_bot.preprocess import convert_number_to_word
from sklearn.metrics.pairwise import cosine_similarity


a_file = open("data.pkl", "rb")
se_dict = pickle.load(a_file)

embedding = {}

start = time.time()
f = open('glove.6B.50d.txt', 'r', encoding="utf8")
for line in f:
    splitLines = line.split()
    word = splitLines[0]
    wordEmbedding = np.array([float(value) for value in splitLines[1:]])
    embedding[word] = wordEmbedding
print("Embeddings Length: ", len(embedding))
end = time.time()
print("Time Taken: ", end - start)

while True:
    print("Enter Query: ")
    start = time.time()
    input_query = input()
    sentence = input_query.lower()
    sentence = convert_number_to_word(sentence)
    sentence = sentence.replace("-", " ")
    sentence = punctuation_removal(sentence)
    words = sentence.split(" ")
    sent_embedding = []
    for word in words:
        w_embedding = np.array(embedding[word])
        sent_embedding.append(w_embedding)
    input_sent_embedding_mean = np.mean(list(sent_embedding), axis=0)

    cosine_dict = {}

    for e in se_dict:
        pointer = e
        a = input_sent_embedding_mean
        b = se_dict[e]
        cosine = cosine_similarity([a], [b], dense_output=True)
        cosine_dict[e] = cosine

    max_cosine_dist_doc = max(cosine_dict, key=cosine_dict.get)

    print("Response: ", max_cosine_dist_doc)
    end = time.time()

    print("Time Taken: ", end - start)