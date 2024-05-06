import numpy as np
from tensorflow import keras

def load_train(path):
    features_train = np.load(path + 'train_features.npy')
    target_train = np.load(path + 'train_target.npy')
    features_train = features_train.reshape(-1, 28, 28, 1) / 255.0
    return features_train, target_train


def create_model(input_shape):
    optimizer = keras.optimizers.Adam(learning_rate=0.0005)
    model = keras.models.Sequential()
    model.add(keras.layers.Conv2D(filters=6, 
                                  kernel_size=(5, 5), 
                                  padding='same', 
                                  activation="relu", 
                                  input_shape=(28, 28, 1)))
    model.add(keras.layers.AvgPool2D(pool_size=(2, 2)))
    model.add(keras.layers.Conv2D(filters=16, kernel_size=(5, 5), activation="relu"))
    model.add(keras.layers.AvgPool2D(pool_size=(2, 2)))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(units=120, activation='relu'))
    model.add(keras.layers.Dense(units=84, activation='relu'))
    model.add(keras.layers.Dense(units=10, activation='softmax'))
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['acc'])
    return model

def train_model(model, train_data, test_data, batch_size=16, epochs=20,
                steps_per_epoch=None, validation_steps=None):
    features_train, target_train = train_data
    features_test, target_test = test_data
    model.fit(features_train, target_train, 
              validation_data=(features_test, target_test),
              batch_size=batch_size,
              epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              shuffle=True,
              verbose=2
              )
    return model 