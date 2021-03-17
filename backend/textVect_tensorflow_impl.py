# https://www.tensorflow.org/api_docs/python/tf/keras/layers/experimental/preprocessing/TextVectorization

# standardize each sample (usually lowercasing + punctuation stripping)
# split each sample into substrings (usually words)
# recombine substrings into tokens (usually ngrams)
# index tokens (associate a unique int value with each token)
# transform each sample using this index, either into a vector of ints or a dense float vector.

import tensorflow as tf
from tensorflow.python.keras.layers.preprocessing.text_vectorization import TextVectorization

from tokenizer import word_tokens

text_dataset = tf.data.Dataset.from_tensor_slices(word_tokens)

max_features = 5000
max_len = 4 # Sequence length to pad the vector.
embedding_dims = 2

vectorize_layer = TextVectorization(
    max_tokens=max_features,
    output_mode='int',
    output_sequence_length=max_len
)

vectorize_layer.adapt(text_dataset.batch(64))
model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(1,), dtype=tf.string))
model.add(vectorize_layer)
input_data = word_tokens
print(model.predict(input_data))
