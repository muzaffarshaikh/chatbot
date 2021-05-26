# import tensorflow as tf
# from tensorflow.python.keras.layers.preprocessing.text_vectorization import TextVectorization
#
#
# def getVectors(words):
#     text_dataset = tf.data.Dataset.from_tensor_slices(words)
#     max_features = 5000
#     max_len = 4  # Sequence length to pad the vector.
#     embedding_dims = 2
#     vectorize_layer = TextVectorization(
#         max_tokens=max_features,
#         output_mode='int',
#         output_sequence_length=max_len
#     )
#     vectorize_layer.adapt(text_dataset.batch(64))
#     model = tf.keras.models.Sequential()
#     model.add(tf.keras.Input(shape=(1,), dtype=tf.string))
#     model.add(vectorize_layer)
#     input_data = words
#     d = model.predict(input_data)
#     x = []
#     for q in d:
#         r = (q[0])
#         ra = [r]
#         x.append(ra)
#     return x


# from sklearn.feature_extraction.text import TfidfVectorizer
#
# from file_reader import read_intents_file
# from data_preprocess import punctuation_removal
# from nltk.tokenize import sent_tokenize
#
# TfidfVectorizerObject = TfidfVectorizer()
#
# intents = read_intents_file()
#
# sent_tokens = []
#
# for intent in intents['intents']:
#     for pattern in intent['patterns']:
#         # pattern = pattern.lower()
#         pattern = punctuation_removal(pattern)
#         s = sent_tokenize(pattern)
#         sent_tokens.append(s)
#
# print(sent_tokens)
#
# tfidf = TfidfVectorizerObject.fit_transform(sent_tokens)
# print(tfidf)
#
# ar = tfidf.toarray()
# for a in ar:
#     print(a)
# import tflearn as tf
# from input_data import x_train, y_train
#
# network_layers = tf.input_data(shape=[None, len(x_train[0])])
# # network_layers = tf.embedding(incoming=network_layers, input_dim=10, output_dim=4)
# network_layers = tf.fully_connected(network_layers, 10)
# network_layers = tf.fully_connected(network_layers, len(y_train[0]), activation='softmax')
# network_layers = tf.regression(network_layers, optimizer='adam', learning_rate=0.01)
# model = tf.DNN(network_layers, tensorboard_verbose='3', tensorboard_dir='tf_logs')
# his = model.fit(x_train, y_train, n_epoch=100, batch_size=8, show_metric=True)


