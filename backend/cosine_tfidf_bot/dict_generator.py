import pickle
import string
import time

from cosine_tfidf_bot.preprocess import convert_number_to_word
from file_read_txt import sent_tokens
import numpy as np


translator = str.maketrans('', '', string.punctuation)
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


se_dict = {}

for entry in sent_tokens:
    t = entry.lower()
    t = convert_number_to_word(t)
    t = t.replace("-", " ")
    t = t.replace("/", " ")
    t = t.replace("@", " ")
    sentence = t.translate(translator)

    pointer = sentence
    words = sentence.split(" ")
    sent_embedding = []
    for word in words:
        print(word)
        w_embedding = np.array(embedding[word])
        sent_embedding.append(w_embedding)
    sent_embedding_mean = np.mean(list(sent_embedding), axis=0)
    se_dict[pointer] = sent_embedding_mean

a_file = open("data.pkl", "wb")
pickle.dump(se_dict, a_file)
a_file.close()

a_file = open("data.pkl", "rb")
se_dict = pickle.load(a_file)
print(type(se_dict))