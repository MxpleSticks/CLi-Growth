import plotext as plt
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

def showResults(portfolioAssets, finalBalance, yearlyData):
    allocTable = Table(show_header=True, header_style='bold cyan')
    allocTable.add_column('symbol')
    allocTable.add_column('Weight', justify='right')

    for i in portfolioAssets:
        allocTable.add_row(i['symbol'], f"{i['weight'] * 100:.0f}")

    growthTable = Table(show_header=True, header_style="bold magenta")
    growthTable.add_column('Year')
    growthTable.add_column('Balance', justify='right')

    years = []
    balances = []

    for i in yearlyData:
        growthTable.add_row(str(i['year']), f"${i['balance']:,.2f}")
        years.append(i['year'])
        balances.append(i['balance'])
    
    innerGrid = Table.grid(padding=6)
    innerGrid.add_row(allocTable, growthTable)

    content = Group(f"[bold green]Final Balance: ${finalBalance:,.2f}[/bold green]", innerGrid)
    
    summaryPanel = Panel(content, title="[bold blue]Portfolio Growth Summary[/bold blue]", width=70)

    plt.clf()
    plt.plot(years, balances, marker='hd')
    plt.title("Portfolio Growth")

    low = min(balances)
    high = max(balances)
    step = (low + high) / 4

    ticks = [low, low + step, low + (2 * step), low + (3 * step), high]
    labels = [f"${int(x):,}" for x in ticks]

    plt.yticks(ticks, labels)


    plt.plotsize(60,20)
    plt.theme('clear')

    plotAnsiString = plt.build()
    plotRenderable = Text.from_ansi(plotAnsiString)

    masterGrid = Table.grid(padding=4)
    masterGrid.add_row(summaryPanel, plotRenderable)

    console.print(masterGrid)

def exportToPDF(portfolioAssets, finalBalance, yearlyData):
    pass