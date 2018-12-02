from keras.preprocessing import image
from keras.applications import resnet50
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D, Input
from keras.optimizers import Adam
from keras.datasets import cifar10
import numpy as np

base_model = resnet50.ResNet50

(x_train, y_train), (_, _) = cifar10.load_data()

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

model.fit(x_train, y_train,
          epochs=2,
          batch_size=50,
          shuffle=False,
          validation_data=(x_train, y_train))


for layer in model.layers[:132]:
	layer.trainable = False
for layer in model.layers[132:]:
	layer.trainable = True

model.layers[175].trainable = False
model.layers[176].trainable = False
model.layers[177].trainable = False

model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(lr=0.0001),
              metrics=['acc'])

model.fit(x_train, y_train,
          epochs=2,
          batch_size=50,
          shuffle=False,
          validation_data=(x_train, y_train))
