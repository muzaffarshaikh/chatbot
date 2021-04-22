import tensorflow as tf

from vectorizer import arr
from vectorizer import tfidf

tensor = tf.reshape(arr, [10, -1])

print(tensor)

# for t in tensor:
#     print(t)
