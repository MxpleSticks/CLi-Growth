import plotext as plt
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table

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

    for i in yearlyData:
        growthTable.add_row(str(i['year']), f"${i['balance']:,.2f}")

    sideBySideGrid = Table.grid(padding=6)
    sideBySideGrid.add_row(allocTable, growthTable)

    content = Group(
        f"[bold green]Final Balance: ${finalBalance:,.2f}[/bold green]", sideBySideGrid)
    
    console.print(Panel(content, title="[bold blue]Portfolio Growth Summary[/bold blue]", width=70))