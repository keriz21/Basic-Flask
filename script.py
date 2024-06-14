from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post-data', methods=['POST'])
def post_data():
    data = request.json
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    
    if temperature is not None and humidity is not None:
        response = {
            'status': 'success',
            'data': {
                'temperature': temperature,
                'humidity': humidity
            }
        }
    else:
        response = {
            'status': 'fail',
            'message': 'Invalid data received'
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
