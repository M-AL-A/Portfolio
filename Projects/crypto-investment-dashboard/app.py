import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
from utils.api_helpers import fetch_crypto_data  # Import your API helper function

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

# Fetch live market data from CoinGecko
try:
    market_data = fetch_crypto_data()
    market_df = pd.DataFrame(market_data)  # Convert API response to DataFrame
except Exception as e:
    market_df = pd.DataFrame()
    print(f"Error fetching market data: {e}")

# Create a sample portfolio chart
if not portfolio_data.empty:
    portfolio_chart = px.pie(
        portfolio_data,
        names="Asset",
        values="Allocation",
        title="Portfolio Allocation"
    )
else:
    portfolio_chart = {}

# Layout for the dashboard
app.layout = html.Div([
    html.H1("Crypto Investment Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.H2("Portfolio Allocation"),
        dcc.Graph(figure=portfolio_chart),
    ], style={"marginBottom": "50px"}),

    html.Div([
        html.H2("Live Market Data"),
        dcc.DataTable(
            id="market-table",
            columns=[
                {"name": "Name", "id": "name"},
                {"name": "Symbol", "id": "symbol"},
                {"name": "Current Price", "id": "current_price"},
                {"name": "Market Cap", "id": "market_cap"}
            ],
            data=market_df[["name", "symbol", "current_price", "market_cap"]].to_dict("records") if not market_df.empty else [],
            styleTable={"overflowX": "auto"}
        ),
    ]),
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

