import rich
import yfinance as yf

print("======================")
print("Welcome to CLi Growth!")
print("======================")
print("<This is a simple CLI tool to help you calculate stock exponential growth>\n")
print("Please enter the following details to calculate your stock growth:")

initialInvestment = float(input("1. Initial Investment Amount (in USD): "))
stockSymbol = input("2. Stock symbol (e.g., AAPL, TSLA):")
monthlyContribution = float(input("3. Monthly Contribution Amount (in USD):"))
compoundFrequency = input("4. Compound Frequency (e.g., monthly, quarterly, annually):")