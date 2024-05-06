from tensorflow import keras

def load_train(path):
    train_datagen = keras.preprocessing.image.ImageDataGenerator(
        validation_split=0.25,
        rescale=1./255,
        horizontal_flip=True, 
        vertical_flip=True, 
        rotation_range=90, 
        width_shift_range=0.2, 
        height_shift_range=0.2
        )
    train_datagen_flow = train_datagen.flow_from_directory(
        path,
        target_size=(150, 150),
        batch_size=16,
        class_mode='sparse',
        subset='training',
        seed=1337)
    return train_datagen_flow

def create_model(input_shape):
    optimizer = keras.optimizers.Adam(learning_rate=0.0001)
    model = keras.models.Sequential()
    model.add(keras.layers.Conv2D(filters=6, kernel_size=(5, 5), padding='same', activation="relu", input_shape=input_shape))
    model.add(keras.layers.AvgPool2D(pool_size=(2, 2)))
    model.add(keras.layers.Conv2D(filters=16, kernel_size=(5, 5), activation="relu"))
    model.add(keras.layers.AvgPool2D(pool_size=(2, 2)))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(units=120, activation='relu'))
    model.add(keras.layers.Dense(units=84, activation='relu'))
    model.add(keras.layers.Dense(units=12, activation='softmax'))
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['acc'])
    return model

def train_model(model, train_data, test_data, batch_size=None, epochs=10, steps_per_epoch=None, validation_steps=None):
    model.fit(train_data, 
              validation_data=test_data,
              batch_size=batch_size,
              epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              shuffle=True,
              verbose=2)
    return model 