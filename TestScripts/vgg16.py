from keras.preprocessing import image
from keras.applications import vgg16
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D, Input
from keras.optimizers import Adam
from keras.datasets import cifar10
import numpy as np
import sys

if __name__ == "__main__":

  index = int(sys.argv[1])

  print("STARTING TRAINING WITH IMAGE NUMBER : {}".format(index))

  epochs = 20

  base_model = vgg16.VGG16

  (x_train, y_train), (_, _) = cifar10.load_data()

  x_train = x_train[index]
  x_train = np.expand_dims(x_train, axis=0)

  y_train = y_train[index]

  base_model = base_model(weights='imagenet', include_top=False, input_shape=(32,32,3))
  x = base_model.output
  x = GlobalAveragePooling2D()(x)
  x = Dense(1024, activation='relu')(x)
  predictions = Dense(100, activation='softmax')(x)
  model = Model(inputs=base_model.input, outputs=predictions)
  for layer in base_model.layers:
      layer.trainable = False

  model.compile(loss='sparse_categorical_crossentropy',
                optimizer=Adam(lr=0.0001),
                metrics=['acc'])

  x_train = vgg16.preprocess_input(x_train)

  model.fit(x_train, y_train,
            epochs=epochs,
            batch_size=1,
            shuffle=False,
            validation_data=(x_train, y_train))

  for layer in model.layers[:11]:
  	layer.trainable = False
  for layer in model.layers[11:]:
  	layer.trainable = True

  model.layers[19].trainable = False
  model.layers[20].trainable = False
  model.layers[21].trainable = False

  model.compile(loss='sparse_categorical_crossentropy',
                optimizer=Adam(lr=0.0001),
                metrics=['acc'])

  model.fit(x_train, y_train,
            epochs=epochs,
            batch_size=1,
            shuffle=False,
            validation_data=(x_train, y_train))