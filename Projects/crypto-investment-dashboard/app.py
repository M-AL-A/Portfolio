import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
from utils.api_helpers import fetch_crypto_prices, get_portfolio_value  # Import helper functions

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Crypto Investment Dashboard"

# Load Ledger Live portfolio data
try:
    portfolio_data = pd.read_csv("data/ledger_portfolio.csv")
    portfolio_data["Allocation"] = portfolio_data["Value"] / portfolio_data["Value"].sum() * 100  # Example calculation
except FileNotFoundError:
    portfolio_data = pd.DataFrame(columns=["Asset", "Value", "Allocation"])
    print("Warning: Portfolio data file not found.")

# Example portfolio data for testing (if portfolio_data is empty)
if portfolio_data.empty:
    portfolio_data = pd.DataFrame({
        "Asset": ["bitcoin", "ethereum", "cardano"],
        "Value": [0.5, 1.2, 1000]
    })
    portfolio_data["Allocation"] = portfolio_data["Value"] / portfolio_data["Value"].sum() * 100

# Fetch live market data and update portfolio values
try:
    crypto_ids = portfolio_data["Asset"].tolist()
    crypto_prices = fetch_crypto_prices(crypto_ids)  # Use helper function to fetch prices

    # Add live prices to portfolio and calculate total values
    portfolio_data["Live Price"] = portfolio_data["Asset"].map(
        lambda x: crypto_prices.get(x, {}).get("usd", 0)
    )
    portfolio_data["Live Value"] = portfolio_data["Value"] * portfolio_data["Live Price"]

except Exception as e:
    portfolio_data["Live Price"] = 0
    portfolio_data["Live Value"] = 0
    print(f"Error updating portfolio with live data: {e}")

# Create portfolio allocation chart
portfolio_chart = px.pie(
    portfolio_data,
    names="Asset",
    values="Allocation",
    title="Portfolio Allocation"
)

# Layout for the dashboard
app.layout = html.Div([
    html.H1("Crypto Investment Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.H2("Portfolio Allocation"),
        dcc.Graph(figure=portfolio_chart),
    ], style={"marginBottom": "50px"}),

    html.Div([
        html.H2("Live Portfolio Value"),
        dcc.DataTable(
            id="portfolio-table",
            columns=[
                {"name": "Asset", "id": "Asset"},
                {"name": "Value", "id": "Value"},
                {"name": "Live Price (USD)", "id": "Live Price"},
                {"name": "Live Value (USD)", "id": "Live Value"}
            ],
            data=portfolio_data.to_dict("records"),
            styleTable={"overflowX": "auto"}
        ),
    ]),
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
