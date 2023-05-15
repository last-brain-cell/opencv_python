import pickle
from keras.models import load_model
from keras.datasets import mnist
import numpy as np
from keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()

num_classes = 10
input_shape = (28, 28, 1)

x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

model = load_model("/Users/naad/PycharmProjects/opencv_python/Learn/TFMetal/model.h5")
input_sample = np.expand_dims(x_test[1], axis=0)  # Add an extra dimension for the batch
prediction = model.predict(input_sample)
print(prediction.argmax(axis=1) + 1)
