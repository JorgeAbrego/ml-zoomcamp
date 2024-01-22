import requests
import json
import time

# get the start time
st = time.time()

# URL of the Flask web service
url = 'http://localhost:9696/predict'

# Example data in the format expected by your model
# Replace this with the actual feature names and sample values
#data = {'text': "great product, I love how it works every day. I need more products like this."}
data = {'text': "I can't believe you made this product, It's the worst I've ever tried."}

# Sending a POST request to the Flask web service
response = requests.post(url, json=data)

# Parsing the response
if response.status_code == 200:
    probability = response.json()['probability']
    prediction = response.json()['prediction']
    print("Prediction:", prediction)
    print("Probability:", probability)
else:
    print("Failed to retrieve prediction. Status Code:", response.status_code)
    
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print(f'Execution time: {elapsed_time} seconds')