import plotext as plt
from pathlib import Path
from fpdf import FPDF
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
    downloadsPath = Path.home() / "Downloads"
    filePath = downloadsPath / "Portfolio Growth Report"

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font('Helvetica', 'B', 18)
    pdf.cell(0, 10, 'CLi Growth Report', ln=True, align='C')
    pdf.ln(5)

    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 8, f"Final Projected Balance: ${finalBalance:,.2f}", ln=True)
    pdf.ln(5)

    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 8, "Portfolio Allocations", ln=True)

    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(60, 7, 'Stock Symbol', border=1)
    pdf.cell(40, 7, 'Weight', border=1, ln=True)

    pdf.set_font('Helvetica', '', 10)
    for i in portfolioAssets:
        pdf.cell(60, 7, i['symbol'], border=1)
        pdf.cell(40, 7, f'{i['weight'] * 100:.1f}%', border=1, ln=True)

    pdf.ln(8)

    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 8, 'Yearly Growth Breakdown', ln=True)

    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 7, 'year', border=1)
    pdf.cell(60, 7, 'Balance', border=1, ln=True)

    pdf.set_font('Helvetica', '', 10)
    for i in yearlyData:
        pdf.cell(40, 7, str(i['year']), border=1)
        pdf.cell(60, 7, f'${i['balance']:,.2f}', border=1, ln=True)
    
    pdf.output(str(filePath))
    console.print(f"\n[bold green]Report successfully saved to you downloads folder: '{filePath}'![/bold green]")