import coffeeData

money = 0.0


def get_money():
    return money


def set_money(amount):
    global money
    money = round(get_money() + amount, 2)


def calculate_coin():
    coin_list = {"dollar": 1, "quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
    amount_inserted = 0.00
    print("\nInsert Coin:")
    for coin in coin_list:
        while True:
            try:
                insert_coin = input(f"{coin}: ")
                if insert_coin == "":
                    amount_inserted += 0.0 * coin_list[coin]
                else:
                    amount_inserted += float(insert_coin) * coin_list[coin]
                break
            except ValueError:
                print("Oops!  That was no valid amount.  Try again...")
    return amount_inserted


def enough_money(coffee_type):
    inserted_amount = calculate_coin()
    if inserted_amount == required_money(coffee_type):
        set_money(inserted_amount)
        return True
    elif inserted_amount > required_money(coffee_type):
        change = round(inserted_amount - required_money(coffee_type), 2)
        gain = inserted_amount - change
        set_money(gain)
        print(f"\nHere is ${change} dollars in change")
        return True
    elif inserted_amount == 0:
        print("0 coin inserted")
    else:
        print(f"Sorry that's not enough money. Money refunded. You need ${required_money(coffee_type)} for {coffee_type}")
        return False


def required_money(coffee_type):
    return coffeeData.MENU[coffee_type]["cost"]
