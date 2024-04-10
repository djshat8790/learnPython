from replit import clear

bid = {}
more_user = True
highest_bidder = ""
highest_bid_price = 0
while more_user:
    bidder_name = input("What is your name?\n")
    bid_price = int(input("What is your bid price\n"))
    bid[bidder_name] = bid_price
    if bid_price > highest_bid_price:
        highest_bid_price = bid_price
        highest_bidder = bidder_name
    answer = input("Are there other users to bid?\n")
    if answer == "no":
        more_user = False
        print(f"The winner is {highest_bidder} with highest price of ${highest_bid_price}")
    elif answer == "yes":
        clear()


