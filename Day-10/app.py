from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

model_path = "models/model.pkl"
model = joblib.load(model_path)

# Define a Flask route for generating predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # assuming input data is in JSON format
    input_data = data['input_data']  # assuming the input data is passed as an array
    app.logger.info('Received input data: %s', input_data)
    prediction = model.predict([input_data])  # assuming model.predict() expects a 2D array
    app.logger.info('Generated prediction: %s', prediction)
    return jsonify({'prediction': prediction.tolist()})


@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)