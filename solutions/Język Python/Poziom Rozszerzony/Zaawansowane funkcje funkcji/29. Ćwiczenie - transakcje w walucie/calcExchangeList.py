def calcExchangeList(exRates, transactions, currency):
    trans = list(filter(lambda i: i[1] == currency, transactions))
    rates = exRates[currency]
    return list(map(lambda x: round(float(x[0]) * float(rates),2) ,trans))
    