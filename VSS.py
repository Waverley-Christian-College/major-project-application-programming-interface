import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt



# Your Tiingo API token
API_TOKEN = "5296eb9cb95697ef016ac7de004f18c24ecfad7c"
print(f"This is my API token {API_TOKEN}")

# Parameters
symbol = input("Enter the stock symbol (e.g., AAPL, MSFT): ").upper()
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

url = f"https://api.tiingo.com/tiingo/daily/{symbol}/prices"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token {API_TOKEN}"
}
params = {
    "startDate": start_date,
    "endDate": end_date,
    "resampleFreq": "monthly",  # Monthly data
}

# Make the request
response = requests.get(url, headers=headers, params=params)
data = response.json()
formatted_json = json.dumps(data, indent = 4) #json.dumps allows the json file to be a string


# Extract dates and closing prices
dates = [entry["date"][:10] for entry in data]
closes = [entry["close"] for entry in data]

# Algorithm for Volatility Scoring System (VSS)
print(f"Number of months checked: {len(data)}") # Counting the number of months in the data
highs = [entry["high"] for entry in data] # Extracting all high prices from each entry
lows = [entry["low"] for entry in data] # Extracting all low prices from each entry
for entry in data:
    get_each_month_price = f"Month: {entry['date'][:7]}, High: {entry['high']}, Low: {entry['low']}" # :7 means first 7 digits of the date (YYYY-MM) # entry high or low means highest and lowest prices for each month
total_highs = sum(highs) # Summing all high prices
total_lows = sum(lows) # Summing all low prices



# Plotting
plt.figure(figsize=(20, 5))
plt.plot(dates, closes, marker='o')
plt.title(f"{symbol} Closing Prices")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
plt.tight_layout()
plt.savefig("stock_chart_tiingo.png")
