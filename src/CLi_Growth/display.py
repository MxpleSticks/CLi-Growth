def showResults(stockSymbol, finalBalance, yearlyData):
    print("-- Growth Summary --")
    print(f"Your final balance with {stockSymbol} is, {finalBalance}!!!")

    for i in yearlyData:
        print(f"{i['year']} ${i['balance']}")