import tkinter as tk
from tkinter import messagebox
from portfolio import Portfolio
from api_utils import fetch_prices_for_portfolio

portfolio = Portfolio()

# Define functions
def add_stock():
    ticker = ticker_entry.get().upper()
    shares = int(shares_entry.get())
    purchase_price = float(purchase_price_entry.get())
    portfolio.add_stock(ticker, shares, purchase_price)
    messagebox.showinfo("Success", f"Added {ticker} to portfolio.")
    update_portfolio_display()

def remove_stock():
    ticker = ticker_entry.get().upper()
    portfolio.remove_stock(ticker)
    messagebox.showinfo("Success", f"Removed {ticker} from portfolio.")
    update_portfolio_display()

def update_prices():
    price_data = fetch_prices_for_portfolio(portfolio)
    portfolio.update_current_prices(price_data)
    messagebox.showinfo("Updated", "Stock prices updated.")
    update_portfolio_display()

def update_portfolio_display():
    portfolio_text.delete("1.0", tk.END)
    for index, row in portfolio.stocks.iterrows():
        portfolio_text.insert(tk.END, f"{row['Ticker']} - Shares: {row['Shares']}, "
                                      f"Purchase Price: ${row['Purchase Price']}, "
                                      f"Current Price: ${row['Current Price']}, "
                                      f"Total Value: ${row['Total Value']}\n")

# Create and configure the main app window
app = tk.Tk()
app.title("Stock Portfolio Tracker")
app.geometry("500x400")  # Set the window to a 600x600 square size
app.configure(bg="#f0f4f7")

# Styles
label_font = ("Arial", 12, "bold")
button_font = ("Arial", 10, "bold")
text_font = ("Arial", 10)
label_color = "#2b3a42"
button_bg = "#4c96d7"
button_fg = "#ffffff"
entry_bg = "#ffffff"

# Ticker Entry
ticker_label = tk.Label(app, text="Ticker Symbol", font=label_font, fg=label_color, bg="#f0f4f7")
ticker_label.grid(row=0, column=0, padx=5, pady=5)
ticker_entry = tk.Entry(app, bg=entry_bg)
ticker_entry.grid(row=0, column=1, padx=5, pady=5)

# Shares Entry
shares_label = tk.Label(app, text="Number of Shares", font=label_font, fg=label_color, bg="#f0f4f7")
shares_label.grid(row=1, column=0, padx=5, pady=5)
shares_entry = tk.Entry(app, bg=entry_bg)
shares_entry.grid(row=1, column=1, padx=5, pady=5)

# Purchase Price Entry
purchase_price_label = tk.Label(app, text="Purchase Price", font=label_font, fg=label_color, bg="#f0f4f7")
purchase_price_label.grid(row=2, column=0, padx=5, pady=5)
purchase_price_entry = tk.Entry(app, bg=entry_bg)
purchase_price_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(app, text="Add Stock", command=add_stock, font=button_font, bg=button_bg, fg=button_fg)
add_button.grid(row=3, column=0, padx=5, pady=5)

remove_button = tk.Button(app, text="Remove Stock", command=remove_stock, font=button_font, bg=button_bg, fg=button_fg)
remove_button.grid(row=3, column=1, padx=5, pady=5)

update_button = tk.Button(app, text="Update Prices", command=update_prices, font=button_font, bg=button_bg, fg=button_fg)
update_button.grid(row=3, column=2, padx=5, pady=5)

# Portfolio Display Text
portfolio_text = tk.Text(app, width=60, height=15, font=text_font, bg="#e6eff5", fg="#3d4d5a")
portfolio_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Run the GUI loop
app.mainloop()
