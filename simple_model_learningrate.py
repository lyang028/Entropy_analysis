import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import numpy as np


def create_data_set(labels,amount):
    # input image dimensions
    # the data, split between train and test sets
    (x_train, y_index_train), (x_test, y_index_test) = mnist.load_data()
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255

    x_train_out = []
    y_index_train_out = []
    for i in labels:
        idx = y_index_train == i
        x_sub = x_train[idx]
        y_sub = y_index_train[idx]
        x_train_out.extend(x_sub[:amount])
        y_index_train_out.extend(y_sub[:amount])
    y_train = keras.utils.to_categorical(y_index_train_out, 10)
    y_test = keras.utils.to_categorical(y_index_test, 10)
    return  np.array(x_train_out),x_test,y_train,y_test
def create_network(learningrate = 0.0001):
    input_shape = (28, 28, 1)
    model = Sequential()
    model.add(Conv2D(3, kernel_size=(3, 3),
                     activation='relu',
                     input_shape=input_shape))
    # model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    # # #extra layer

    # extra layer
    model.add(Flatten())
    model.add(Dense(32, activation='relu'))
    # model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(lr=learningrate),
                  metrics=['accuracy'])

    return model