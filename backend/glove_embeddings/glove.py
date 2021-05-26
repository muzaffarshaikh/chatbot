import numpy as np
import time


def embeddings():
    start = time.time()
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
    end = time.time()
    print("time taken", end - start)
    f.close()
    return embeddings_dict
