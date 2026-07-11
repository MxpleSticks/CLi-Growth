import rich
import yfinance as yf

print("======================")
print("Welcome to CLi Growth!")
print("======================")
print("<This is a simple CLI tool to help you calculate stock exponential growth>\n")
print("Please enter the following details to calculate your stock growth:")

while True:
    try:
        initialInvestment = float(input("1. Initial Investment Amount (in USD): "))
        if initialInvestment < 0:
            print("Invalid input. Please enter a valid number for the Initial Investment Amount (in USD): ")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for the Initial Investment Amount (in USD): ")

while True:
    stockSymbol = input("2. Stock symbol (e.g., AAPL, TSLA):")
    if not stockSymbol:
        print("Invalid input. Please enter a valid stock symbol (e.g., AAPL, TSLA): ")
        continue

    print(f"Verifying stock symbol '{stockSymbol}'...")
    tickerData = yf.Ticker(stockSymbol)
    try:
        if tickerData.history(period="1d").empty:
            print(f"Invalid stock symbol '{stockSymbol}'. Please enter a valid stock symbol (e.g., AAPL, TSLA): ")
            continue
        break
    except:
        print(f"Error connecting to yfinance for '{stockSymbol}'. please try again")



monthlyContribution = float(input("3. Monthly Contribution Amount (in USD):"))
compoundFrequency = input("4. Compound Frequency (e.g., monthly, quarterly, annually):")