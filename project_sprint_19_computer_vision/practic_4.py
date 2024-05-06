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
    backbone = keras.applications.resnet.ResNet50(input_shape=(150, 150, 3),
                    weights='/datasets/keras_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5',
                    include_top=False) 
    model = keras.models.Sequential()
    model.add(backbone)
    model.add(keras.layers.GlobalAveragePooling2D())
    model.add(keras.layers.Dense(12, activation='softmax'))

    optimizer = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['acc']) 

    return model

def train_model(model, train_data, test_data, batch_size=None, epochs=7, steps_per_epoch=None, validation_steps=None):
    model.fit(train_data, 
              validation_data=test_data,
              batch_size=batch_size,
              epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              shuffle=True,
              verbose=2)
    return model 