import requests

API_KEY = "BZ8SH8S5UDMQGRVK"  # Replace with your actual API key

BASE_URL = "https://www.alphavantage.co/query"

def get_stock_price(ticker):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": ticker,
        "interval": "5min",
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    try:
        return float(data['Time Series (5min)'].values()[0]['4. close'])
    except KeyError:
        return None

def fetch_prices_for_portfolio(portfolio):
    prices = {}
    for ticker in portfolio.stocks['Ticker']:
        prices[ticker] = get_stock_price(ticker)
    return prices
