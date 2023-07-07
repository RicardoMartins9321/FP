"""
This function takes in a list called "stocks" and first prints the header row of the table. 
Then it iterates through the list of tuples, unpacking the variables "company", "city", "open_price", "close_price", and "volume" from each tuple. 
It then calculates the appreciation of the share as a percentage by taking the difference between the closing price and the opening price, 
dividing by the opening price, and multiplying by 100. It rounds this value to 1 decimal places and adds the "%" symbol to the end. 
It then prints the values of the "company", "city", "open_price", "close_price", "volume" and "appreciation" variables formatted 
with the .ljust() method to align the columns."""

def printStocks(stocks):
    print("Company".ljust(15) + "City".ljust(15) + "Open".ljust(15) + "Close".ljust(15) + "Volume".ljust(15) + "Appreciation")
    for stock in stocks:
        company, city, open_price, close_price, volume = stock
        appreciation = round((close_price - open_price) / open_price * 100, 1)
        appreciation = str(appreciation) + "%"
        print(company.ljust(15) + city.ljust(15) + str(round(open_price, 2)).ljust(15) + str(round(close_price, 2)).ljust(15) + str(volume).ljust(15) + appreciation)

"""
This function takes in two arguments, "stocks" which is a list of tuples containing information
about shares of different companies traded on stock exchanges in different cities and "city" 
which is the city for which the function will return the list of companies and stock volumes.

The function uses a list comprehension to iterate through each tuple in "stocks", 
and for each tuple, if the second element of the tuple (city) is equal to the given "city"
it will return a tuple of the first element of the tuple (company) and the fifth element of the 
tuple (volume) as an element in the final list. This list is returned as the final result."""
def companyVolume(stocks, city):
    return [(x[0], x[4]) for x in stocks if x[1] == city]

def load(fname):
   stocks = []
   with open(fname) as f:
      for line in f:
         company, city, opening, closing, volume = line.strip().split('\t')
         stocks.append((company, city, float(opening), float(closing), int(volume)))
   return stocks

def main():
    stocks = [ ('INTC', 'London', 34.249, 34.451, 1792860),
                ('TSLA', 'London', 221.33, 229.63, 398520),
                ('EA', 'Paris', 72.63, 68.98, 1189510),
                ('INTC', 'Tokyo', 33.22001, 34.28999, 4509110),
                ('TSLA', 'Paris', 217.35, 217.75, 252500),
                ('ATML', 'Frankfurt', 8.23, 8.36, 810440),
                ]

    printStocks(stocks)
    
    """
    This line of code uses the built-in "sorted" function to sort the list of tuples "stocks" by the first element of each tuple 
    (which represents the company name) and, in cases where two or more tuples have the same company name, 
    by the fifth element of each tuple (which represents the traded volume) in descending order.

    The "key" argument of the "sorted" function takes in a lambda function that specifies the sorting criteria. 
    The lambda function takes in the variable "x" (representing each tuple in the list) and returns a tuple of the first element and the 
    negative fifth element of each tuple, which represents the sorting order of the company name and the traded volume respectively.

    The sorted list of stocks can be accessed by the variable sorted_stocks."""
    sorted_stocks = sorted(stocks, key=lambda x: (x[0], -x[4]))
    print(sorted_stocks)
    print()
    city = input("Choose a city: ")
    print(companyVolume(stocks, city.title()))
    print()
    print(load("Exercícios extra 3/stocks.txt"))

if __name__ == "__main__":
    main()