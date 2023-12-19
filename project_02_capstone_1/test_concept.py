# %%
import tensorflow.lite as tflite
import numpy as np
from PIL import Image

def load_and_preprocess_image(image_path):
    with Image.open(image_path) as img:
        img = img.resize((224, 224), Image.LANCZOS)
    img_array = np.array(img, dtype='float32')
    img_array /= 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

image_path = './data/test//Potato/1179.jpg'
X = load_and_preprocess_image(image_path)

interpreter = tflite.Interpreter(model_path='vegetables-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

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

print(f"Class:{classes[np.argmax(preds)]}")
print(f"Probability:{round(preds[0][np.argmax(preds)],4)}")
