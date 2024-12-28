Crypto Investment Dashboard
Your ultimate tool for tracking and optimizing cryptocurrency investments with integration for Ledger Live.

## Description
The Crypto Investment Dashboard is a web application that helps users:
    - Monitor their cryptocurrency investments.
    - Retrieve live market data for better decision-making.
    - Get trade recommendations based on pre-set thresholds.
    - Visualize their portfolio through dynamic charts.

This project integrates with Ledger Live and uses the CoinGecko API to fetch live market data.

## Features
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
    Open the dashboard and explore:
        - View your portfolio distribution.
        - Check real-time market data.
        - Get actionable trade recommendations.

## File Structure
crypto-dashboard/

├── app.py                  # Main application script

├── data/                   # Directory for data files


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
    - Support for multiple portfolios.
    - Historical trade analysis.
    - Deployment to a live server.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
Created by [Matthew Archer](https://github.com//M-AL-A) - feel free to reach out!




Adding items to the watchlist can be done using curl (command-line tool) or Postman (a graphical interface for API requests). Here's how you can do it using both methods:

Using curl (Command Line)
Open your terminal or command prompt.

Use the following command to send a POST request to the /watchlist/add route:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"symbol": "bitcoin"}' http://127.0.0.1:5000/watchlist/add
Replace "bitcoin" with the symbol of the cryptocurrency you want to add.

You should see a JSON response like this if it’s successful:

json
Copy code
{
    "message": "bitcoin added to the watchlist."
}
Using Postman
Install Postman (if not already installed):

Download it from Postman’s website.
Open Postman:

Launch the application after installation.
Set Up the Request:

Click on "New" → "Request".
Name the request (e.g., "Add to Watchlist").
Select the POST method.
Enter the URL: http://127.0.0.1:5000/watchlist/add.
Add the JSON Body:

Go to the "Body" tab.
Select "raw".
Choose "JSON" from the dropdown (on the right side).
Enter the JSON payload:
json
Copy code
{
    "symbol": "bitcoin"
}
Send the Request:

Click "Send".
You’ll see the response in the lower panel.
Verify the Addition
After adding, you can view the current watchlist by sending a GET request to /watchlist:

Using curl:
bash
Copy code
curl http://127.0.0.1:5000/watchlist
Using Postman:
Create a new GET request.
Set the URL to http://127.0.0.1:5000/watchlist.
Click "Send".
This will return the current watchlist in JSON format.

