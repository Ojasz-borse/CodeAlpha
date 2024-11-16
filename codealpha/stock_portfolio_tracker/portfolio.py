import pandas as pd

class Portfolio:
    def __init__(self):
        self.stocks = pd.DataFrame(columns=['Ticker', 'Shares', 'Purchase Price', 'Current Price', 'Total Value'])

    def add_stock(self, ticker, shares, purchase_price):
        new_stock = pd.DataFrame([{
            'Ticker': ticker,
            'Shares': shares,
            'Purchase Price': purchase_price,
            'Current Price': 0.0,
            'Total Value': 0.0
        }])
        self.stocks = pd.concat([self.stocks, new_stock], ignore_index=True)

    def remove_stock(self, ticker):
        self.stocks = self.stocks[self.stocks['Ticker'] != ticker]

    def update_current_prices(self, price_data):
        for i, row in self.stocks.iterrows():
            if row['Ticker'] in price_data:
                self.stocks.at[i, 'Current Price'] = price_data[row['Ticker']]
                self.stocks.at[i, 'Total Value'] = row['Shares'] * price_data[row['Ticker']]
