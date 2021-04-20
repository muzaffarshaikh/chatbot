import numpy as np
# from glove import embeddings


def getSentenceGloVector(sentence, glove_embeddings, word_vector_size, sentence_vector_size):
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


# g = getSentenceGloVector("hello how are you doing", embeddings(), 5, 30)
# print(g)
# print(len(g))
