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
    "resampleFreq": input("Frequency (e.g., daily, weekly, monthly, annually): "),
}

# Make the request
response = requests.get(url, headers=headers, params=params)
data = response.json()
formatted_json = json.dumps(data, indent = 4) #json.dumps allows the json file to be a string



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
plt.savefig("AAPL.png")
