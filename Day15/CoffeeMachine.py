import coffeeData
import check_resources
import check_coin


def coffee_machine():
    machine = True
    while machine:
        print("\nAvailable Coffee: Espresso, Latte or Cappuccino")
        coffee_type = input("What would you like?\n").lower()
        if check_resources.check_resources(coffee_type):
            if check_coin.enough_money(coffee_type):
                if coffee_type == "espresso":
                    check_resources.remaining_water -= check_resources.required_water(coffee_type)
                    check_resources.remaining_coffee -= check_resources.required_coffee(coffee_type)
                    print(f"Here is your {coffee_type}. Enjoy!\n")
                elif coffee_type == "latte" or coffee_type == "cappuccino":
                    check_resources.remaining_water -= check_resources.required_water(coffee_type)
                    check_resources.remaining_coffee -= check_resources.required_coffee(coffee_type)
                    check_resources.remaining_milk -= check_resources.required_milk(coffee_type)
                    print(f"Here is your {coffee_type}. Enjoy!\n")
                else:
                    print("1. Please enter the correct coffee.")
        elif coffee_type == "off":
            machine = False
        elif coffee_type == "report":
            print(f"Water: {check_resources.remaining_water}ml")
            print(f"Milk: {check_resources.remaining_milk}ml")
            print(f"Coffee: {check_resources.remaining_coffee}g")
            print(f"Money: ${check_coin.get_money()}\n")
        elif coffee_type == "refill":
            check_resources.refill_resources()
        else:
            print("To refill the resources. Type 'refill'")


coffee_machine()