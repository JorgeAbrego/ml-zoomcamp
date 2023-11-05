import requests
import json

# URL of the Flask web service
url = 'http://localhost:9696/predict'

# Example data in the format expected by your model
# Replace this with the actual feature names and sample values
data = {'age': 30, 
        'height_cm': 175, 
        'weight_kg': 75, 
        'waist_cm': 89, 
        'eyesight_left': 1.2,
        'eyesight_right': 1.2, 
        'hearing_left': 1, 
        'hearing_right': 148, 
        'systolic': 80,
        'relaxation': 97, 
        'fasting_blood_sugar': 164, 
        'cholesterol': 54, 
        'triglyceride': 90,
        'hdl': 142, 
        'ldl': 19.8, 
        'hemoglobin': 120, 
        'urine_protein': 2.0, 
        'serum_creatinine': 61, 
        'ast': 19,
        'alt': 22, 
        'gtp': 19, 
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