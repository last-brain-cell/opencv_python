import numpy as np
import tensorflow as tf
from keras import Sequential
from keras.datasets import mnist
from keras.utils import to_categorical
import datetime


# enabling GPU growth to allocate memory on-demand
physical_devices = tf.config.list_physical_devices('GPU')
print("Num GPUs Available:", len(physical_devices))
for device in physical_devices:
    tf.config.experimental.set_memory_growth(device, True)

if len(physical_devices) > 0:
    print("Available GPUs: " + str(physical_devices))

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# Load the data and split it between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")


# convert class vectors to binary class matrices
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

model = Sequential(
    [
        tf.keras.layers.Conv2D(32, (5, 5), kernel_initializer='he_uniform', activation='relu', padding='same', input_shape=input_shape),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D((2, 2)),

        tf.keras.layers.Conv2D(64, (5, 5), kernel_initializer='he_uniform', activation='relu', padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Dropout(0.1),

        tf.keras.layers.Conv2D(128, (5, 5), kernel_initializer='he_uniform', activation='relu', padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D((2, 2)),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(10, kernel_initializer='he_uniform', activation='softmax')
    ]
)

datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range=10,  # rotate images randomly within 10 degrees
    zoom_range=0.1,     # zoom images randomly within 10%
    width_shift_range=0.1,  # shift images horizontally randomly within 10%
    height_shift_range=0.1,  # shift images vertically randomly within 10%
    shear_range=0.1,    # shear images randomly within 10 degrees
    horizontal_flip=False,  # flip images horizontally randomly
    vertical_flip=False   # flip images vertically randomly
)

datagen.fit(x_train)

model.summary()

model.compile(loss="categorical_crossentropy", optimizer='adam', metrics=["accuracy"])

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(
    datagen.flow(x_train, y_train, batch_size=50),
    epochs=15,
    callbacks=[tensorboard_callback]
)

# model.save("modelz.h5")
# tensorboard dev upload --logdir \ 'logs/fit'