import rich
import yfinance as yf
from computation import portfolioRate, calculateCompoundGrowth
from display import showResults


print("======================")
print("Welcome to CLi Growth!")
print("======================")
print("<This is a simple CLI tool to help you calculate compound stock growth>\n")
print("Please enter the following details to calculate your stock growth:")

while True:
    try:
        initialInvestment = float(input("1. Initial Investment Amount (in USD): "))
        if(initialInvestment < 0):
            print("Invalid input. Please enter a valid number for the Initial Investment Amount (in USD).")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for the Initial Investment Amount (in USD).")

print("\nplease enter your portfolio allocation (must equal 100%)")
portfolioAssets = []
totalWeight = 0.0

while totalWeight < 100.0:
    stockSymbol = input('2. Enter stock symbol (e.g. AAPL, TSLA) (current total: {}%):'.format(totalWeight)).upper()
    if not stockSymbol:
        continue
    print('verifying {}...'.format(stockSymbol))
    try:
        if(yf.Ticker(stockSymbol).history(period='1d').empty):
            print("invalid symbol. try again.")
            continue
    except:
        print("error connecting. Try again.")
        continue
    
    try:
        assetWeight = float(input("enter percentage for {} (e.g. 50 for 50%):".format(stockSymbol)))
        if(assetWeight <= 0 or totalWeight + assetWeight > 100.0):
            print("invalid weight or exceeds 100%")
            continue
        
        portfolioAssets.append({'symbol': stockSymbol, 'weight': assetWeight / 100.0})
        totalWeight = totalWeight + assetWeight
    except:
        print('Enter a valid number')

while True:
    try:
        monthlyContribution = float(input("3. Monthly Contribution Amount (in USD):"))
        if(monthlyContribution < 0):
            print("Invalid input. Please enter a valid Monthly Contribution Amount (in USD).")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid Monthly Contribution Amount (in USD).")


validFrequency = ["monthly", "quarterly", "annually"]
while True:
    compoundFrequency = input("4. Compound Frequency (e.g., monthly, quarterly, annually): ").strip().lower()
    if(compoundFrequency in validFrequency):
        break
    else:
        print(f"Please choose from: {', '.join(validFrequency)}")


while True:
    try:
        years = int(input("5. Time horizon in years (e.g. 5, 40, etc...): "))
        if(years <= 0):
            print("Time horizon must be at least 1 year.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")


print("\nCalculating growth...")

raw = portfolioRate(portfolioAssets)
inflation = 0.025
rate = max(0.0, raw - inflation)

finalBalance, yearlyData = calculateCompoundGrowth(initialInvestment, monthlyContribution, compoundFrequency, years, rate)

showResults(portfolioAssets, finalBalance, yearlyData)