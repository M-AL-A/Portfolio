from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return 'Welcome to the Crypto Investment Dashboard!'

# Define the watchlist route to get all items in the watchlist
@app.route('/watchlist', methods=['GET'])
def get_watchlist():
    try:
        with open('crypto_watchlist.json', 'r') as file:
            watchlist = json.load(file)
        return jsonify(watchlist)
    except FileNotFoundError:
        return jsonify({"message": "Watchlist is empty or file not found."})

# Define a route to add a cryptocurrency to the watchlist
@app.route('/watchlist/add', methods=['POST'])
def add_to_watchlist():
    data = request.get_json()
    symbol = data.get('symbol')

    if not symbol:
        return jsonify({"message": "Symbol is required."}), 400

    try:
        with open('crypto_watchlist.json', 'r') as file:
            watchlist = json.load(file)
    except FileNotFoundError:
        watchlist = {}

    if symbol in watchlist:
        return jsonify({"message": f"{symbol} is already in the watchlist."}), 400

    watchlist[symbol] = {"symbol": symbol}
    with open('crypto_watchlist.json', 'w') as file:
        json.dump(watchlist, file, indent=4)

    return jsonify({"message": f"{symbol} added to the watchlist."})

# Define a route to remove a cryptocurrency from the watchlist
@app.route('/watchlist/remove', methods=['POST'])
def remove_from_watchlist():
    data = request.get_json()
    symbol = data.get('symbol')

    if not symbol:
        return jsonify({"message": "Symbol is required."}), 400

    try:
        with open('crypto_watchlist.json', 'r') as file:
            watchlist = json.load(file)
    except FileNotFoundError:
        return jsonify({"message": "Watchlist is empty."})

    if symbol not in watchlist:
        return jsonify({"message": f"{symbol} is not in the watchlist."}), 404

    del watchlist[symbol]
    with open('crypto_watchlist.json', 'w') as file:
        json.dump(watchlist, file, indent=4)

    return jsonify({"message": f"{symbol} removed from the watchlist."})

# Define a route to fetch live data for cryptocurrencies in the watchlist
@app.route('/watchlist/data', methods=['GET'])
def get_watchlist_data():
    try:
        with open('crypto_watchlist.json', 'r') as file:
            watchlist = json.load(file)
    except FileNotFoundError:
        return jsonify({"message": "Watchlist is empty."})

    crypto_data = {}
    for symbol in watchlist:
        response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd')
        if response.status_code == 200:
            data = response.json()
            if symbol in data:
                crypto_data[symbol] = data[symbol]
            else:
                crypto_data[symbol] = {"error": "Not found in API."}
        else:
            crypto_data[symbol] = {"error": "Failed to fetch data."}

    return jsonify(crypto_data)

if __name__ == '__main__':
    app.run(debug=True)
