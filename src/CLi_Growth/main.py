from rich.console import Console
import yfinance as yf
from computation import portfolioRate, calculateCompoundGrowth
from display import showResults, exportToPDF

console = Console()

console.print("[bold blue]======================[/bold blue]")
console.print("[bold blue]Welcome to CLi Growth![/bold blue]")
console.print("[bold blue]======================[/bold blue]")
console.print("[italic]<This is a simple CLI tool to help you calculate compound stock growth>[/italic]\n")
print("Please enter the following details to calculate your stock growth:")

while True:
    try:
        initialInvestment = float(input("1. Initial Investment Amount (in USD): "))
        if(initialInvestment < 0):
            console.print("[red]Invalid input. Please enter a valid number for the Initial Investment Amount (in USD).[/red]")
            continue
        break
    except ValueError:
        console.print("[red]Invalid input. Please enter a valid number for the Initial Investment Amount (in USD).[/red]")

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
            console.print("[red]invalid symbol. try again.[/red]")
            continue
    except:
        console.print("[red]error connecting. Try again.[/red]")
        continue
    
    try:
        assetWeight = float(input("enter percentage for {} (e.g. 50 for 50%):".format(stockSymbol)))
        if(assetWeight <= 0 or totalWeight + assetWeight > 100.0):
            console.print("[red]invalid weight or exceeds 100%[/red]")
            continue
        
        portfolioAssets.append({'symbol': stockSymbol, 'weight': assetWeight / 100.0})
        totalWeight = totalWeight + assetWeight
    except:
        console.print('[red]Enter a valid number[/red]')

while True:
    try:
        monthlyContribution = float(input("3. Monthly Contribution Amount (in USD):"))
        if(monthlyContribution < 0):
            console.print("[red]Invalid input. Please enter a valid Monthly Contribution Amount (in USD).[/red]")
            continue
        break
    except ValueError:
        console.print("[red]Invalid input. Please enter a valid Monthly Contribution Amount (in USD).[/red]")


validFrequency = ["monthly", "quarterly", "annually"]
while True:
    compoundFrequency = input("4. Compound Frequency (e.g., monthly, quarterly, annually): ").strip().lower()
    if(compoundFrequency in validFrequency):
        break
    else:
        console.print(f"[red]Please choose from: {', '.join(validFrequency)}[/red]")


while True:
    try:
        years = int(input("5. Time horizon in years (e.g. 5, 40, etc...): "))
        if(years <= 0):
            console.print("[red]Time horizon must be at least 1 year.[/red]")
            continue
        break
    except ValueError:
        console.print("[red]Invalid input. Please enter a whole number.[/red]")


console.print("[bold yellow]\nCalculating growth...[/bold yellow]")

raw = portfolioRate(portfolioAssets)
inflation = 0.025
rate = max(0.0, raw - inflation)

finalBalance, yearlyData = calculateCompoundGrowth(initialInvestment, monthlyContribution, compoundFrequency, years, rate)

showResults(portfolioAssets, finalBalance, yearlyData)

createPDF = input("Would you like to download a PDF report of these results? (y/n): ").strip().lower()
if(createPDF in ['y', 'yes']):
    exportToPDF(portfolioAssets, finalBalance, yearlyData)

console.input("[red]\nPress enter to exit[/red]")