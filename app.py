from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import pickle
import zstandard as zstd
import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from src.utilts import decompress,load_data
from src.pipeline.predict_pipeline import make_prediction

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json()
    
    # Validate input
    if 'data' not in data:
        return jsonify({'error': 'Invalid input, missing "data" key'}), 400

    # Predict and return result
    output = make_prediction(data['data'])
    return jsonify({'predicted_price': output})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form data
        data = {
                'airline': request.form.get('airline'),
                'flight': request.form.get('flight'),
                'source_city': request.form.get('source_city'),
                'departure_time': request.form.get('departure_time'),
                'stops': request.form.get('stops'),
                'arrival_time': request.form.get('arrival_time'),
                'destination_city': request.form.get('destination_city'),
                'class': request.form.get('class'),
                'duration': float(request.form.get('duration', 0)),
                'days_left': float(request.form.get('days_left', 0))
            }
      
        # Predict
        output = make_prediction(data)
        return render_template("home.html", prediction_text=f"The  price of flight is {output:.2f} INR")
    except Exception as e:
        return render_template("home.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, host='127.0.0.1', port=5000)
