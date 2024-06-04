import math
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

PORT = 5050
HOUR = 60

def calculate_calories(cph, duration):
    return math.floor((duration / HOUR) * cph)

@app.route('/conversions', methods=['GET'])
def get_conversions():
    activity1_cph = request.args.get("activity1_cph", type=int)
    activity2_cph = request.args.get("activity2_cph", type=int)
    duration = request.args.get("duration", type=int)

    calories1 = calculate_calories(activity1_cph, duration) 
    calories2 = calculate_calories(activity2_cph, duration) 
    
    response = jsonify({"activity1": calories1, "activity2": calories2})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
