import yfinance as yf

def getHistoricalReturnRate(stockSymbol):
    ticker = yf.Ticker(stockSymbol)
    hist = ticker.history(period="max")

    if(hist.empty or len(hist) < 2):
        return 0.0
    
    firstPrice = hist['Close'].iloc[0]
    lastPrice = hist['Close'].iloc[-1]

    startDate = hist.index[0]
    endDate = hist.index[-1]

    years = (endDate - startDate).days / 365.25

    if(years <= 0):
        return 0.0
    
    cagr = (lastPrice / firstPrice) ** (1 / years) - 1
    return cagr


def calculateCompoundGrowth(initialInvestment, monthlyContribution, compoundFrequency, years, annualRate):
    freqMap = {"monthly" : 12, "quarterly" : 4, "annually" : 1}
    compoundPerYear = freqMap.get(compoundFrequency, 1)

    balance = initialInvestment
    yearlyData = []

    monthsPerCompound = 12 // compoundPerYear

    for i in range(1, years + 1):
        for j in range(1, 13):
            balance += monthlyContribution

            if(j % monthsPerCompound == 0):
                balance += balance * (annualRate / compoundPerYear)
        
        yearlyData.append({"year" : i, "balance" : balance})
    
    return balance, yearlyData