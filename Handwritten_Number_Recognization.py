# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10kuohOOfbQFXfZAO473p-3DSaBCHisUw
"""

import numpy as np
import matplotlib.pyplot as plt

import keras
from keras.datasets import mnist

from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout

from keras.callbacks import EarlyStopping , ModelCheckpoint

(x_train, y_train), (x_test,y_test) = mnist.load_data()
x_train.shape , y_train.shape , x_test.shape , y_test.shape

def plot_input_img(i):
  plt.imshow(x_train[i], cmap = 'binary')
  plt.title(y_train[i])
  plt.show()

for i in range(10):
  plot_input_img(i)

# pre process the images

x_train = x_train.astype(np.float32)/255
x_test = x_test.astype(np.float32)/255

#Reshape

x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

model = Sequential()

model.add(Conv2D(32,(3,3), input_shape = (28,28,1), activation='relu'))
model.add(MaxPool2D(2,2))

model.add(Conv2D(64,(3,3), activation='relu'))
model.add(MaxPool2D(2,2))

model.add(Flatten())

model.add(Dropout(0.25))
model.add(Dense(10, activation="softmax"))

model.summary()

model.compile(optimizer='adam', loss = keras.losses.categorical_crossentropy , metrics=['accuracy'])

#callback


es = EarlyStopping(monitor='val_acc', min_delta=0.01, patience=4, verbose=1)

mc = ModelCheckpoint("./bestmodel.h5", monitor="val_acc", varbose=1, save_best_only = True)

cb = [es,mc]

his = model.fit(x_train, y_train, epochs= 5, validation_split= 0.3, callbacks = cb)

model_S = keras.models.load_model("D:\\")

score = model_S.evaluate(x_test, y_test)

print(f" the model accuracy is{score[1]}")