def readStocks(filename):
    stocks = []
    with open(filename, 'r') as file:
        next(file)  # Pula o cabeçalho
        for line in file:
            company, date, opening, high, low, close, volume = line.strip().split('\t')
            stock = (company, date, float(opening), float(high), float(low), float(close), int(volume))
            stocks.append(stock)
    return stocks

def totalVolume(lst):
    volume_dict = {}
    for stock in lst:
        company, _, _, _, _, _, volume = stock
        if company in volume_dict:
            volume_dict[company] += volume
        else:
            volume_dict[company] = volume
    return volume_dict

def maxValorization(lst):
    valorization_dict = {}
    for stock in lst:
        company, date, opening, _, _, close, _ = stock
        valorization = (close / opening - 1) * 100
        if date in valorization_dict:
            if valorization > valorization_dict[date][1]:
                valorization_dict[date] = (company, valorization)
        else:
            valorization_dict[date] = (company, valorization)
    return valorization_dict

def stocksByDateByName(lst):
    stocks_dict = {}
    for stock in lst:
        company, date, opening, high, low, close, volume = stock
        if date in stocks_dict:
            stocks_dict[date][company] = (opening, high, low, close, volume)
        else:
            stocks_dict[date] = {company: (opening, high, low, close, volume)}
    return stocks_dict

def portfolioValue(portfolio, date, stocks_dict):
    total_value = 0.0
    if date in stocks_dict:
        stocks = stocks_dict[date]
        for company, quantity in portfolio.items():
            if company in stocks:
                _, _, _, close, _ = stocks[company]
                total_value += close * quantity
    return total_value


def main():
    filename = 'FP_AulasPráticas/aula07/nasdaq.csv'
    stocks = readStocks(filename)
    print("Total Volume:")
    print(totalVolume(stocks))
    print("Max Valorization:")
    print(maxValorization(stocks))
    print("Stocks by Date and Name:")
    print(stocksByDateByName(stocks))
    print("Portfolio Value:")
    portfolio = {'NFLX': 100, 'CSCO': 80}
    date = '2022-01-05'
    stocks_dict = stocksByDateByName(stocks)
    print(portfolioValue(portfolio, date, stocks_dict))

if __name__ == '__main__':
    main()

