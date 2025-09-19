from flask import Flask, request, jsonify, render_template
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from src.pipeline.predict_pipeline import make_prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json()

    # Check if 'data' exists
    if 'data' not in data:
        return jsonify({'error': 'Missing data'}), 400

    try:
        prediction = make_prediction(data['data'])
        return jsonify({'predicted_price': float(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get JSON data from AJAX request
#         data = request.get_json()

#         if not data:
#             return jsonify({'error': 'No input data provided'}), 400

#         # Predict using your pipeline
#         predicted_price = make_prediction(data)

#         # Return JSON response
#         return jsonify({'prediction': round(predicted_price, 2)})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)

