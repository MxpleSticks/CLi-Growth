def showResults(portfolioAssets, finalBalance, yearlyData):
    print("-- Portfolio Growth Summary --")
    print("your final balance is: ${}".format(round(finalBalance, 2)))
    
    for i in portfolioAssets:
        print('- {}: {}%'.format(i['symbol'], i['weight'] * 100))

    for i in yearlyData:
        print('Year {}: ${}'.format(i['year'],round(i['balance'], 2)))