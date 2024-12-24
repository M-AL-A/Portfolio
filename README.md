# Portfolio
My personal portfolio.


~ Project 01 ~

# Crypto Investment Dashboard
Your ultimate tool for tracking and optimizing cryptocurrency investments with integration for Ledger Live.

## Description
The Crypto Investment Dashboard is a web application that helps users:
    - Monitor their cryptocurrency investments.
    - Retrieve live market data for better decision-making.
    - Get trade recommendations based on pre-set thresholds.
    - Visualize their portfolio through dynamic charts.

This project integrates with Ledger Live and uses the CoinGecko API to fetch live market data.

## Features
    - **Ledger Live Integration**: Automatically fetch portfolio data.
    - **Real-Time Market Data**: Live updates for crypto prices using CoinGecko API.
    - **Trade Recommendations**: Suggestions based on price trends and thresholds.
    - **Interactive Dashboard**: Dynamic charts and tables for portfolio visualization.

## Installation
    1. Clone the repository:
        git clone https://github.com/your-username/crypto-dashboard.git
        cd crypto-dashboard

    2. Create and activate a virtual environment:
          python -m venv venv
          source venv/bin/activate    # Linux/Mac
          venv\Scripts\activate       # Windows

    3. Install dependencies:
          pip install -r requirements.txt

    4. Run the application:
          python app.py

    5. Open your browser and navigate to http://127.0.0.1:8050/.

## Usage
    1. Export your Ledger Live portfolio data as a CSV file.
    2. Place the file in the root directory of this project.
    3. Open the dashboard and explore:
        - View your portfolio distribution.
        - Check real-time market data.
        - Get actionable trade recommendations.

## File Structure
crypto-dashboard/
├── app.py                  # Main application script
├── data/                   # Directory for data files
│   └── ledger_portfolio.csv  # Example portfolio CSV
├── static/                 # Directory for static assets
│   ├── style.css           # Custom styles
│   ├── logo.png            # Logo
├── templates/              # HTML templates for rendering pages
│   └── base.html
├── utils/                  # Helper modules
│   ├── api_helpers.py      # Functions to fetch market data
│   └── trade_logic.py      # Logic for trade recommendations
├── screenshots/            # Images for README
├── requirements.txt        # Python dependencies
├── README.md               # Detailed project description
└── LICENSE                 # License information
               # License for the project

## Screenshots
![Portfolio Distribution](screenshots/portfolio_chart.png)
![Trade Recommendations](screenshots/trade_recommendations.png)

## Technologies Used
    - Python 3.x
    - Dash for the dashboard
    - Flask for backend integration
    - Pandas for data manipulation
    - CoinGecko API for market data
    - Plotly for interactive charts

## Future Features
    - Full Ledger Live API integration.
    - Support for multiple portfolios.
    - Historical trade analysis.
    - Deployment to a live server.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
Created by [Matthew Archer](https://github.com//M-AL-A) - feel free to reach out!