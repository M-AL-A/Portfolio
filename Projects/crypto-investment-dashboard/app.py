from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)

# Path to the JSON file to store the watchlist
WATCHLIST_FILE = "data/crypto_watchlist.json"

# Load or initialize the watchlist
def load_watchlist():
    try:
        with open(WATCHLIST_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_watchlist(watchlist):
    with open(WATCHLIST_FILE, 'w') as f:
        json.dump(watchlist, f)

@app.route('/watchlist', methods=['GET'])
def get_watchlist():
    watchlist = load_watchlist()
    return jsonify(watchlist)

@app.route('/watchlist/add', methods=['POST'])
def add_crypto():
    data = request.json
    symbol = data.get('symbol')
    if not symbol:
        return jsonify({'error': 'Symbol is required'}), 400

    watchlist = load_watchlist()
    if symbol in watchlist:
        return jsonify({'message': f'{symbol} is already in the watchlist.'}), 200
    
    watchlist.append(symbol)
    save_watchlist(watchlist)
    return jsonify({'message': f'{symbol} added to the watchlist.'}), 201

@app.route('/watchlist/remove', methods=['POST'])
def remove_crypto():
    data = request.json
    symbol = data.get('symbol')
    if not symbol:
        return jsonify({'error': 'Symbol is required'}), 400

    watchlist = load_watchlist()
    if symbol not in watchlist:
        return jsonify({'message': f'{symbol} is not in the watchlist.'}), 404

    watchlist.remove(symbol)
    save_watchlist(watchlist)
    return jsonify({'message': f'{symbol} removed from the watchlist.'}), 200

@app.route('/watchlist/data', methods=['GET'])
def get_crypto_data():
    watchlist = load_watchlist()
    if not watchlist:
        return jsonify({'message': 'No cryptocurrencies in the watchlist.'}), 200

    api_url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ','.join(watchlist),
        'vs_currencies': 'usd'
    }
    response = requests.get(api_url, params=params)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data.'}), 500

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
