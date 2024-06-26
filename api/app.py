from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calculate_bmi(weight, height, metric='metric'):
    """Calculate the Body Mass Index (BMI) of a person."""
    if metric == 'english':
        # Convert pounds to kilograms
        weight_kg = weight * 0.453592
        # Convert feet and inches to meters
        height_m = height * 0.0254
    else:
        weight_kg = weight
        height_m = height

    return weight_kg / (height_m ** 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi_route():
    data = request.json
    weight = float(data['weight'])
    height = float(data['height'])
    metric = data['metric']
    bmi = calculate_bmi(weight, height, metric)
    response = jsonify({'bmi': bmi})
    # Set CORS headers
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response

if __name__ == '__main__':
    app.run(debug=True)
