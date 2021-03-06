from keras.preprocessing import image
from keras.applications import inception_v3
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D, Input
from keras.optimizers import Adam
from keras.datasets import cifar10
import cv2
import numpy as np

base_model = inception_v3.InceptionV3

(x_train, y_train), (_, _) = cifar10.load_data()

x_train = x_train[:100]
y_train = y_train[:100]

print(x_train.shape)

data_upscaled = np.zeros((100, 299, 299, 3))

for i, img in enumerate(x_train):
    # im = img.transpose((1, 2, 0))
    large_img = cv2.resize(
        img, dsize=(299, 299), interpolation=cv2.INTER_CUBIC)
    data_upscaled[i] = large_img

x_train = data_upscaled

base_model = base_model(weights='imagenet', include_top=False, input_shape=(299,299,3))
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

x_train = inception_v3.preprocess_input(x_train)

model.fit(x_train, y_train,
          epochs=1,
          batch_size=50,
          shuffle=False,
          validation_data=(x_train, y_train))

for layer in model.layers[:249]:
	layer.trainable = False
for layer in model.layers[249:]:
	layer.trainable = True

model.layers[311].trainable = False
model.layers[312].trainable = False
model.layers[313].trainable = False

model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(lr=0.0001),
              metrics=['acc'])

model.fit(x_train, y_train,
          epochs=1,
          batch_size=50,
          shuffle=False,
          validation_data=(x_train, y_train))