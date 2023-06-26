#!flask/bin/python
from flask import Flask, request, jsonify
import onnxruntime as rt
import numpy as np
import json


# Create a Flask application
app = Flask(__name__)

# Hello world endpoint
@app.route('/')
def hello():
    return "<p>Hello, This is a Specific Microservice for a deployed ONNX Model!</p>"

# Verify the status of the microservice

@app.route('/health')
def healthjson():
    mydata = {
        "status" : "UP" 
    }
    return jsonify(mydata)


# Load the ONNX model from a URL
sess = rt.InferenceSession("model/onnx-model/cumulocity_classification_model_3.onnx")

# Define an API endpoint that will receive input data from a client

@app.route('/predict', methods=['POST'])

def predict():
    # Get the input data from the request
    input_data = request.json["inputs"]

    # Convert JSON object to Python dictionary
    #python_data = json.loads(input_data)

    # Get all values from dictionary as a list (sorted according to the key names to ensure the correct sequence of x,y,z values)
    #list_values = list(input_data.values())
    list_values = [value for key, value in sorted(input_data.items())]

    
    # Convert the input data to a numpy array (Suitable for Streaming Analytics)
    #input_array = np.array(input_data, dtype=np.float32)
    input_array = np.array(list_values).reshape((1, 3, 1)).astype(np.float32)

    # Get the names of the input and output nodes of the ONNX model
    input_name = sess.get_inputs()[0].name
    output_name = sess.get_outputs()[0].name
    
    # Perform the prediction using the ONNX model
    output = sess.run([output_name], {input_name: input_array})
    
    # Convert the prediction output to a JSON object
    output_data = {"output": output[0].tolist()}
    
    # Return the prediction output as a JSON response
    return jsonify(output_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)