class StockAverage:

    def __init__(self):
        self.number_of_shares_buying = 0
        self.number_of_shares_selling = 0
        self.current_share_price = 0
        self.current_holding = 0
        self.current_average_price = 0

    def average_cost_basis_buying(self):
        self.current_holding = float(input(f"How many shares are you holding currently: "))
        self.current_average_price = float(input(f"What is your current average price per share: "))
        self.number_of_shares_buying = float(input(f"Number of shares buying: "))
        self.current_share_price = float(input(f"current share price: "))

        average_cost_basis_buying = ((self.current_holding * self.current_average_price + self.number_of_shares_buying * self.current_share_price)
                                     / (self.current_holding + self.number_of_shares_buying))
        return average_cost_basis_buying

    def average_cost_basis_selling(self):
        pass

    def average(self, price, shares):
        return price * shares / shares


stock = StockAverage()
print(stock.average_cost_basis_buying())



