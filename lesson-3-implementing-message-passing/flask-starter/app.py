import json
from flask import Flask, jsonify, request
from .services import retrieve_orders, create_orders


app = Flask(__name__)

@app.route('/api/orders/computers', methods=['GET', 'POST'])
def computers():
    if request.method == 'GET':
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        return jsonify(create_orders(request.json))
    else:
        raise Exception('Unsupported HTTP request type.')

@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

if __name__ == '__main__':
    app.run()
