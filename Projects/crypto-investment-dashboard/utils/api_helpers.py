import requests

# Define the CoinGecko API endpoint
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

def fetch_crypto_prices(crypto_ids):
    """
    Fetches the current prices for the given list of cryptocurrencies from the CoinGecko API.
    
    Args:
        crypto_ids (list of str): List of cryptocurrency IDs (e.g., ['bitcoin', 'ethereum']).

    Returns:
        dict: A dictionary mapping crypto IDs to their current prices (e.g., {'bitcoin': 35000}).
    """
    try:
        # Join crypto IDs into a single string for the API request
        ids = ",".join(crypto_ids)
        response = requests.get(f"{COINGECKO_API_URL}/simple/price", params={"ids": ids, "vs_currencies": "usd"})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching crypto prices: {e}")
        return {}

def get_portfolio_value(portfolio, crypto_prices):
    """
    Calculates the total value of the portfolio based on current prices.

    Args:
        portfolio (dict): User portfolio (e.g., {'bitcoin': 0.5, 'ethereum': 1.2}).
        crypto_prices (dict): Current crypto prices (e.g., {'bitcoin': 35000, 'ethereum': 2400}).

    Returns:
        float: Total portfolio value in USD.
    """
    total_value = 0
    for crypto, amount in portfolio.items():
        price = crypto_prices.get(crypto, 0)
        total_value += amount * price
    return total_value

