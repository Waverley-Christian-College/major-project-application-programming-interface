import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt

# Your Tiingo API token
API_TOKEN = "5296eb9cb95697ef016ac7de004f18c24ecfad7c"
# Parameters
start_date = "2025-01-01"
end_date = "2025-04-01"
# Asking user for how many companies
companies = int(input("How many companies do you want to see? "))
symbols = []
# The .upper() code captilizes the users input
for i in range(companies):
    symbol = input(f"Enter a company #{i+1}: ").upper()
    symbols.append(symbol)

fig, ax = plt.subplots(figsize=(12, 6))

for symbol in symbols:
    url = f"https://api.tiingo.com/tiingo/daily/{symbol}/prices"
    headers = {"Authorization": f"Token {API_TOKEN}"}
    params = {"startDate": start_date, "endDate": end_date, "resampleFreq": "daily"}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    dates = [item["date"][:10] for item in data]
    prices = [item["close"] for item in data]

    ax.plot(dates, prices, marker='o', label=symbol)
# Plot
title = " & ".join(symbols) + " Closing Prices"
ax.set_title(title)
ax.set_xlabel("Date")
ax.set_ylabel("Close Price (USD)")
ax.legend()
ax.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
    
# What I changed in the code
'''
axes[1].set_xlabel("Date")
'''
# Label x-axis for the bottom plot only
plt.tight_layout()
plt.show()

# Save figure
plt.savefig("stock_comparison_tiingo.png")

# This is my old line of code that I kept just in case anything wrong
# The process of developing my code from only showing 2 graphs to any amount of companies the user asks for
'''
# Your Tiingo API token
API_TOKEN = "5296eb9cb95697ef016ac7de004f18c24ecfad7c"
# Parameters
symbol = input("What companies do you want? ")
symbolw = input("Choose another company to compare: ")

start_date = "2025-01-01"
end_date = "2025-04-01"

url1 = f"https://api.tiingo.com/tiingo/daily/{symbol}/prices"
url2 = f"https://api.tiingo.com/tiingo/daily/{symbolw}/prices"
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
response1 = requests.get(url1, headers=headers, params=params)
response2 = requests.get(url2, headers=headers, params=params)

# Extract data for both stocks
data1 = response1.json()
data2 = response2.json()
# Extract dates and closing prices
dates1 = [entry["date"][:10] for entry in data1]
closes1 = [entry["close"] for entry in data1]

dates2 = [entry["date"][:10] for entry in data2]
closes2 = [entry["close"] for entry in data2]

# Create a figure with 2 subplots (1 column, 2 rows)
fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=True)  # sharex ensures both graphs have the same x-axis

# First plot (Top: NVDA stock)
axes[0].plot(dates1, closes1, marker='o', color='blue')
axes[0].set_title(f"{symbol} Closing Prices")
axes[0].set_ylabel("Close Price (USD)")
axes[0].grid(True)
axes[0].tick_params(axis="x", rotation=45)  # Rotate x-axis labels for better readability

# Second plot (Bottom: TSLA stock)
axes[1].plot(dates2, closes2, marker='o', color='red')
axes[1].set_title(f"{symbolw} Closing Prices")
axes[1].set_xlabel("Date")
axes[1].set_ylabel("Close Price (USD)")
axes[1].grid(True)
axes[1].tick_params(axis="x", rotation=45)  # Rotate x-axis labels for better readability

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()

# Optionally, save the figure to a file
plt.savefig("stock_comparison_tiingo.png")

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

plt.figure(figsize=(10, 5))
plt.plot(dates, closes, marker='o')
plt.title(f"{symbolw} Closing Prices")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
plt.tight_layout()
plt.savefig("stock_chart_tiingo.png")
url1 = f"https://api.tiingo.com/tiingo/daily/{symbol}/prices"
url2 = f"https://api.tiingo.com/tiingo/daily/{symbolw}/prices"
'''