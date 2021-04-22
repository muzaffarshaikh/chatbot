import tflearn
from tensorflow.python.framework import ops


def create_model(train_features, train_classes):
    ops.reset_default_graph()

    network_layers = tflearn.input_data(shape=[None, len(train_features[0])])
    # network_layers = tflearn.embedding(incoming=network_layers, input_dim=10, output_dim=4)
    network_layers = tflearn.fully_connected(network_layers, 10)
    network_layers = tflearn.fully_connected(network_layers, 10)
    network_layers = tflearn.fully_connected(network_layers, len(train_classes[0]), activation='softmax')
    network_layers = tflearn.regression(network_layers, optimizer='adam', learning_rate=0.01)
    model = tflearn.DNN(network_layers, tensorboard_dir='tflearn_logs')
    model = tflearn.DNN(network_layers, tensorboard_verbose='3')
    model.fit(train_features, train_classes, n_epoch=1000, batch_size=8, show_metric=True)
    return model
