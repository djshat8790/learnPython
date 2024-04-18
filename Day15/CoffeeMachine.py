import coffeeData
import check_resources
import check_coin


def coffee_machine():
    machine = True
    while machine:
        print("\nAvailable Coffee: Espresso, Latte and Cappuccino")
        coffee_type = input("What would you like?\n").lower()
        if coffee_type == "off":
            machine = False
        elif coffee_type == "report":
            print(f"Water: {check_resources.remaining_water}ml")
            print(f"Milk: {check_resources.remaining_milk}ml")
            print(f"Coffee: {check_resources.remaining_coffee}g")
            print(f"Money: ${check_coin.get_money()}\n")
        elif coffee_type == "refill":
            check_resources.refill_resources()
        elif coffee_type == "espresso" or coffee_type == "cappuccino" or coffee_type == "latte":
            if check_resources.check_resources(coffee_type) and check_coin.enough_money(coffee_type):
                if coffee_type == "latte" or coffee_type == "cappuccino":
                    check_resources.remaining_milk -= check_resources.required_milk(coffee_type)
                check_resources.remaining_water -= check_resources.required_water(coffee_type)
                check_resources.remaining_coffee -= check_resources.required_coffee(coffee_type)
                print(f"Here is your {coffee_type}. Enjoy!\n")
        else:
            print("Please enter the correct coffee.")

coffee_machine()
