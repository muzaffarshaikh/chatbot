import numpy as np


def load_embeddings_dict():
    File = 'glove.6B.50d.txt'
    print("Loading Glove Model")
    f = open(File, 'r', encoding="utf8")
    embeddings_dict = {}
    for line in f:
        splitLines = line.split()
        word = splitLines[0]
        wordEmbedding = np.array([float(value) for value in splitLines[1:]])
        embeddings_dict[word] = wordEmbedding
    print(len(embeddings_dict), " words loaded!")
    # print(embeddings_dict)
    return embeddings_dict


def get_w2v(sentence, model):
    """
    :param sentence: inputs a single sentences whose word embedding is to be extracted.
    :param model: inputs glove model.
    :return: returns numpy array containing word embedding of all words    in input sentence.
    """
    return np.array([model.get(val, np.zeros(100)) for val in sentence.split()], dtype=np.float64)
