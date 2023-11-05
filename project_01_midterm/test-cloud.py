import requests
import json

# URL of the Flask web service
url = 'http://srv-smoking-predictor.eba-5yjgjzxt.us-east-1.elasticbeanstalk.com/predict'

# Example data in the format expected by your model
# Replace this with the actual feature names and sample values
data = {
        "age":45,
        "height_cm":170,
        "weight_kg":80,
        "waist_cm":93.0,
        "eyesight_left":1.2,
        "eyesight_right":1.5,
        "hearing_left":1,
        "hearing_right":1,
        "systolic":130,
        "relaxation":80,
        "fasting_blood_sugar":87,
        "cholesterol":215,
        "triglyceride":246,
        "hdl":52,
        "ldl":114,
        "hemoglobin":15.3,
        "urine_protein":1,
        "serum_creatinine":1.0,
        "ast":26,
        "alt":15,
        "gtp":78,
        "dental_caries":0
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