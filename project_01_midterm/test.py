import requests
import json

# URL of the Flask web service
url = 'http://localhost:9696/predict'

# Example data in the format expected by your model
# Replace this with the actual feature names and sample values
data = {'age': 35, 
        'height_cm': 170, 
        'weight_kg': 85, 
        'waist_cm': 0.9, 
        'eyesight_left': 0.9,
        'eyesight_right': 1, 
        'hearing_left': 1, 
        'hearing_right': 118, 
        'systolic': 78,
        'relaxation': 97, 
        'fasting_blood_sugar': 239, 
        'cholesterol': 153, 
        'triglyceride': 70,
        'hdl': 142, 
        'ldl': 19.8, 
        'hemoglobin': 1, 
        'urine_protein': 1.0, 
        'serum_creatinine': 61, 
        'ast': 115,
        'alt': 125, 
        'gtp': 1, 
        'dental_caries': 1
        }

# Sending a POST request to the Flask web service
response = requests.post(url, json=data)

# Parsing the response
if response.status_code == 200:
    probability = response.json()['probability']
    prediction = response.json()['prediction']
    print("Probability:", probability)
    print("Prediction:", prediction)
else:
    print("Failed to retrieve prediction. Status Code:", response.status_code)