import tflearn
from tensorflow.python.framework import ops


def create_model(train_features, train_classes):
    ops.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(train_features[0])])
    net = tflearn.fully_connected(net, 10)
    net = tflearn.fully_connected(net, 10)
    net = tflearn.fully_connected(net, len(train_classes[0]), activation='softmax')
    net = tflearn.regression(net, optimizer='SGD', learning_rate=0.01)
    model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
    model.fit(train_features, train_classes, n_epoch=1000, batch_size=8, show_metric=True)
    return model
