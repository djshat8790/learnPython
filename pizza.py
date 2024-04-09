size = input("Which size of pizza do you want?\n")

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25

pep = input("Do you want pepperoni?\n")

if pep == "y":
    if size == "s":
        bill += 2
    elif size == "m":
        bill += 5
    else:
        bill += 10

cheese = input("Do you want cheese as well?\n")

if cheese == "y":
    if size == "s":
        bill += 5
    elif size == "m":
        bill += 10
    else:
        bill += 15

print (f"Total bill: {bill}")