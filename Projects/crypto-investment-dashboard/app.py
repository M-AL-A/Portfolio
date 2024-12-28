from flask import Flask, jsonify, request, render_template
import requests
import json

app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return render_template('index.html')

# Define the watchlist route to get all items in the watchlist
@app.route('/watchlist', methods=['GET'])
def get_watchlist():
    try:
        with open('./data/crypto_watchlist.json', 'r') as file:
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

    link = f"https://www.coingecko.com/en/coins/{symbol.lower()}"

    try:
        with open('./data/crypto_watchlist.json', 'r') as file:
            watchlist = json.load(file)
    except FileNotFoundError:
        watchlist = {}

    if symbol in watchlist:
        return jsonify({"message": f"{symbol} is already in the watchlist."}), 400

    watchlist[symbol] = {"symbol": symbol, "link": link}
    with open('./data/crypto_watchlist.json', 'w') as file:
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
        with open('./data/crypto_watchlist.json', 'r') as file:
            watchlist = json.load(file)
    except FileNotFoundError:
        return jsonify({"message": "Watchlist is empty."})

    if symbol not in watchlist:
        return jsonify({"message": f"{symbol} is not in the watchlist."}), 404

    del watchlist[symbol]
    with open('./data/crypto_watchlist.json', 'w') as file:
        json.dump(watchlist, file, indent=4)

    return jsonify({"message": f"{symbol} removed from the watchlist."})

if __name__ == '__main__':
    app.run(debug=True)
