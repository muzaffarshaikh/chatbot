import tflearn


def create_model(x_train, y_train, train):
    network_layers = tflearn.input_data(shape=[None, len(x_train[0])])
    network_layers = tflearn.fully_connected(network_layers, 10)
    network_layers = tflearn.fully_connected(network_layers, 10)
    network_layers = tflearn.fully_connected(network_layers, len(y_train[0]), activation='softmax')
    network_layers = tflearn.regression(network_layers, optimizer='adam')
    if train is True:
        model = tflearn.DNN(network_layers, tensorboard_dir='tflearn_logs')
        model.fit(x_train, y_train, n_epoch=1000, batch_size=8, show_metric=True)
    else:
        model = tflearn.DNN(network_layers)
        model.load('./model.tflearn')
    return model
