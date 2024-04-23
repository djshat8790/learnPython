class StockAverage:

    def __init__(self):
        self.number_of_shares_buying = 0
        self.number_of_shares_selling = 0
        self.current_share_price = 0
        self.number_of_shares_bought_initially = 0
        self.price_of_shares_initially = 0

    def average_cost_basis_buying(self):
        self.number_of_shares_bought_initially = float(input(f"Number of shares bought initially: "))
        self.price_of_shares_initially = float(input(f"Initial price of per share: "))
        self.number_of_shares_buying = float(input(f"Number of shares buying: "))
        self.current_share_price = float(input(f"current share price: "))

        average_cost_basis_buying = ((self.number_of_shares_bought_initially * self.price_of_shares_initially + self.number_of_shares_buying * self.current_share_price)
                                     / (self.number_of_shares_bought_initially + self.number_of_shares_buying))
        return average_cost_basis_buying

    def average_cost_basis_selling(self):
        pass

    def average(self, price, shares):
        return price * shares / shares


import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDA&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)


stock = StockAverage()
print(stock.average_cost_basis_buying())
