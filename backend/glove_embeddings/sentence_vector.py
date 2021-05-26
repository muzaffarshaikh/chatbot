import numpy as np

from glove import embeddings

emb = embeddings()
print(len(emb))


def getSentenceGloVectorSum(sentence, glove_embeddings, word_vector_size, sentence_vector_size):
    pointer = sentence
    words = sentence.split(" ")
    sent_embedding = []
    for word in words:
        w_embedding = np.array(glove_embeddings[word])
        w_embedding.resize(word_vector_size)
        for w in w_embedding:
            sent_embedding.append(w)
    np_embedding = np.array(sent_embedding)
    np_embedding.resize(sentence_vector_size)
    return np_embedding


def getSentenceGloVectorMean(sentence, glove_embeddings):
    pointer = sentence
    words = sentence.split(" ")
    sent_embedding = []
    for word in words:
        w_embedding = np.array(glove_embeddings[word])
        sent_embedding.append(w_embedding)
    sent_embedding_mean = np.mean(list(sent_embedding), axis=0)
    return sent_embedding_mean


g = getSentenceGloVectorMean("hello how are you", emb)
print(g)
