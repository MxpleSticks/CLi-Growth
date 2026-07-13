from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns

console = Console()

def showResults(portfolioAssets, finalBalance, yearlyData):
    print("-- Portfolio Growth Summary --")
    print("your final balance is: ${}".format(round(finalBalance, 2)))
    
    for i in portfolioAssets:
        print('- {}: {}%'.format(i['symbol'], i['weight'] * 100))

    for i in yearlyData:
        print('Year {}: ${}'.format(i['year'],round(i['balance'], 2)))