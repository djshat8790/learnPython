import coffeeData

remaining_water = coffeeData.resources["water"]
remaining_milk = coffeeData.resources["milk"]
remaining_coffee = coffeeData.resources["coffee"]


def required_water(coffee_type):
    return coffeeData.MENU[coffee_type]["ingredients"]["water"]


def required_milk(coffee_type):
    return coffeeData.MENU[coffee_type]["ingredients"]["milk"]


def required_coffee(coffee_type):
    return coffeeData.MENU[coffee_type]["ingredients"]["coffee"]


def check_water(resource_coffee_type):
    if required_water(resource_coffee_type) < remaining_water:
        return True
    else:
        return False


def check_coffee(resource_coffee_type):
    if required_coffee(resource_coffee_type) < remaining_coffee:
        return True
    else:
        return False


def check_milk(resource_coffee_type):
    if required_milk(resource_coffee_type) < remaining_milk:
        return True
    else:
        return False


def refill_resources():
    global remaining_water
    global remaining_milk
    global remaining_coffee
    remaining_water = coffeeData.resources["water"]
    remaining_milk = coffeeData.resources["milk"]
    remaining_coffee = coffeeData.resources["coffee"]


def check_resources(resource_coffee_type):
    if resource_coffee_type == "espresso":
        if not check_water(resource_coffee_type):
            print("Sorry there is not enough water.")
            return False
        if not check_coffee(resource_coffee_type):
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    elif resource_coffee_type == "latte" or resource_coffee_type == "cappuccino":
        if not check_water(resource_coffee_type):
            print("Sorry there is not enough water.")
            return False
        if not check_coffee(resource_coffee_type):
            print("Sorry there is not enough coffee.")
            return False
        if not check_milk(resource_coffee_type):
            print("Sorry there is not enough milk.")
            return False
        else:
            return True


