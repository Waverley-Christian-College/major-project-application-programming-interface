import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt

# Your Tiingo API token
API_TOKEN = "5296eb9cb95697ef016ac7de004f18c24ecfad7c"

# Parameters
symbol = "MSFT"
start_date = "2025-04-23"
end_date = "2025-04-29"

url = f"https://api.tiingo.com/tiingo/daily/{symbol}/prices"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token {API_TOKEN}"
}
params = {
    "startDate": start_date,
    "endDate": end_date,
    "resampleFreq": "daily"
}

# Make the request
response = requests.get(url, headers=headers, params=params)
data= response.json()
formatted_json = json.dumps(data, indent = 4) #json.dumps allows the json file to be a string

# Search Function
client = TiingoClient(API_TOKEN)
fetch_prices = client.get_ticker_price(symbol, start_date, end_date, frequency="daily")

# Extract dates and closing prices
dates = [entry["date"][:10] for entry in data]
closes = [entry["close"] for entry in data]

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
