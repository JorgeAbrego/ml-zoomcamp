import pickle

import pandas as pd
from flask import Flask
from flask import request
from flask import jsonify


def load(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

model = load('model_rf.bin')
app = Flask('smoking_classification')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
    
    X =pd.DataFrame([client])
    y_pred = model.predict_proba(X)[0, 1]
    smoker = y_pred >= 0.5
    result = {
        'probability': float(y_pred),
        'prediction': bool(smoker)
    }
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)