import tflite_runtime.interpreter as tflite
import os
import numpy as np
from io import BytesIO
from urllib import request
from PIL import Image


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def prepare_input(x):
    return x / 255.0

interpreter = tflite.Interpreter('vegetables-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def predict(url):
    img = download_image(url)
    img = prepare_image(img, target_size=(224, 224))

    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = prepare_input(X)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()

    preds = interpreter.get_tensor(output_index)

    classes = [
        'Bean',
        'Bitter_Gourd',
        'Bottle_Gourd',
        'Brinjal',
        'Broccoli',
        'Cabbage',
        'Capsicum',
        'Carrot',
        'Cauliflower',
        'Cucumber',
        'Papaya',
        'Potato',
        'Pumpkin',
        'Radish',
        'Tomato'
    ]

    return classes[np.argmax(preds)], preds[0][np.argmax(preds)]


def lambda_handler(event, context):
    url = event['url']
    pred, proba = predict(url)
    result = {
        'prediction': pred,
        'probability':float(proba)
    }

    return result