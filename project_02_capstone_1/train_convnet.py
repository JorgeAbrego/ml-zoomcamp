#!/usr/bin/env python
# coding: utf-8

# Loading modules
import pathlib
from PIL import Image
import os
import tensorflow as tf
from tensorflow.keras import models, layers
from tensorflow.keras.callbacks import EarlyStopping

# Setting constant for training model
SEED = 11
BATCH_SIZE = 32
IMAGE_SIZE = 224
CHANNELS=3
EPOCHS=10

# Loading train and validation datasets
print("Loading datasets")
train_folder = './data/train'
validation_folder = './data/validation'

train_data = tf.keras.utils.image_dataset_from_directory(
    train_folder,
    seed=SEED,
    image_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    shuffle=True
)

val_data = tf.keras.utils.image_dataset_from_directory(
    validation_folder,
    seed=SEED,
    image_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    shuffle=True
)

# Getting classes
class_names = train_data.class_names
num_classes = len(class_names)

# Data procesing before training
print("Procesing datasets before training")
data_augmentation = tf.keras.Sequential([
  layers.RandomFlip("horizontal_and_vertical"),
  layers.RandomRotation(0.2),
])

train_data = train_data.map(
    lambda x, y: (data_augmentation(x, training=True), y)
).prefetch(buffer_size=tf.data.AUTOTUNE)

normalization_layer = tf.keras.layers.Rescaling(1./255)

train_data = train_data.map(lambda x, y: (normalization_layer(x, training=True), y))
val_data = val_data.map(lambda x, y: (normalization_layer(x, training=False), y))

# Setting model architecture
model = models.Sequential([
    layers.Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMAGE_SIZE, IMAGE_SIZE, CHANNELS)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, 3, padding='same', activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(100, activation='relu'),
    layers.Dense(num_classes, activation='softmax'),
])

model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics=['accuracy']
)

# Training ConvNet
print("Training model started")
early_stopping = EarlyStopping(monitor='val_loss', patience=10)

history = model.fit(
    train_data,
    batch_size=BATCH_SIZE,
    validation_data=val_data,
    verbose=1,
    epochs=EPOCHS,
    callbacks=[early_stopping],
)

print("Model training finished")

print('Best accuracy:',max(history.history['accuracy']))

# Converting model to TFlite
print("Exporting model to TFLite")

model_name = "vegetables-model"

converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with open(f"./{model_name}.tflite", 'wb') as f_out:
    f_out.write(tflite_model)
    
print(f"Model exported to:{model_name}.tflite")