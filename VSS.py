import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import time



def hello():
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

    # Calculate Average This will be comapred to the difference 

    # Calculate total of all (highs + lows) for each month
    total_highs_plus_lows = 0 #Reset Variable
    for entry in data:
        highs_plus_lows = entry["high"] + entry["low"] # Add up the highs and the lows
        total_highs_plus_lows += highs_plus_lows # Changing the Variable of total_highs_plus_lows by adding the values of highs_plus_lows together

    # Calculate the average: (sum of all highs + lows) / number of months
    average_highs_plus_lows = total_highs_plus_lows / len(data) # Divide by months 
    # Calculate average minus volatility price for each month

    total_volatility_prices = 0
    for entry in data:
        month = entry["date"][:7]
        highs = entry["high"] # Checks highest price of each month
        lows = entry["low"] # Checks lowest price each month
        volatility_price = highs - lows
        total_volatility_prices += volatility_price # Stores it into total_volatility_prices
        #average_minus_volatility = average_highs_plus_lows - volatility_price 
        

    # Calculate sum of all volatility prices divided by months
    average_volatility = total_volatility_prices / len(data)
    print(f"The price has differed about {average_volatility:.2f} from the average price of {average_highs_plus_lows} over that period of time")

    # Introduce a scale

    if average_volatility <= 10:
        time.sleep(1)
        print("0-10 is really low volatility you will not make that much money")

    elif average_volatility <= 20:
        time.sleep(1)
        print("10-20 is low volatility you would've/will not make that much money back then in the long term")

    elif average_volatility <= 80:
        time.sleep(1)
        print("20-80 is fluctulating volatility where it was/is the best time to invest on a small risk scale")

    elif average_volatility > 80: 
        time.sleep(1)
        print("80> the volatility is high: Invest/Invested on high risk and you will/would've made or lost alot of money")

    time.sleep(5)

    print("Please restart Program to return to home...")

















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
