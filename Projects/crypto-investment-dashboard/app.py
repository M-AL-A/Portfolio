import os
from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

# Define the path to the watchlist file
WATCHLIST_FILE = '/data/crypto_watchlist.json'

# Define a route for the root URL
@app.route('/')
def home():
    return render_template('index.html')

# Define the watchlist route to get all items in the watchlist
@app.route('/watchlist', methods=['GET'])
def get_watchlist():
    if not os.path.exists(WATCHLIST_FILE):
        return jsonify({"message": "Watchlist is empty or file not found."})

    with open(WATCHLIST_FILE, 'r') as file:
        watchlist = json.load(file)
    return jsonify(watchlist)

# Define a route to add a cryptocurrency to the watchlist
@app.route('/watchlist/add', methods=['POST'])
def add_to_watchlist():
    data = request.get_json()
    symbol = data.get('symbol')

    if not symbol:
        return jsonify({"message": "Symbol is required."}), 400

    link = f"https://www.coingecko.com/en/coins/{symbol.lower()}"

    try:
        with open(WATCHLIST_FILE, 'r') as file:
            watchlist = json.load(file)
    except FileNotFoundError:
        watchlist = {}

    if symbol in watchlist:
        return jsonify({"message": f"{symbol} is already in the watchlist."}), 400

    watchlist[symbol] = {"symbol": symbol, "link": link}
    with open(WATCHLIST_FILE, 'w') as file:
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
        with open(WATCHLIST_FILE, 'r') as file:
            watchlist = json.load(file)
    except FileNotFoundError:
        return jsonify({"message": "Watchlist is empty."})

    if symbol not in watchlist:
        return jsonify({"message": f"{symbol} is not in the watchlist."}), 404

    del watchlist[symbol]
    with open(WATCHLIST_FILE, 'w') as file:
        json.dump(watchlist, file, indent=4)

    return jsonify({"message": f"{symbol} removed from the watchlist."})

# Define a route to fetch live data for cryptocurrencies in the watchlist
@app.route('/watchlist/data', methods=['GET'])
def get_watchlist_data():
    if not os.path.exists(WATCHLIST_FILE):
        return jsonify({"message": "Watchlist is empty."})

    with open(WATCHLIST_FILE, 'r') as file:
        watchlist = json.load(file)

    crypto_data = {}
    for symbol, details in watchlist.items():
        response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd')
        if response.status_code == 200:
            data = response.json()
            if symbol in data:
                crypto_data[symbol] = { 
                    "price": data[symbol].get('usd', 'N/A'),
                    "link": details['link']
                }
            else:
                crypto_data[symbol] = {"error": "Not found in API.", "link": details['link']}
        else:
            crypto_data[symbol] = {"error": "Failed to fetch data.", "link": details['link']}

    return jsonify(crypto_data)

if __name__ == '__main__':
    app.run(debug=True)
