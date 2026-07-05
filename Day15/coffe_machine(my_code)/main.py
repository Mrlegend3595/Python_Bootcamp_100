Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def water_enough(type_coffee):
    """returns True if the enough water."""
    return resources["water"] >= Menu[type_coffee]["ingredients"]["water"]

def milk_enough(type_coffee):
    """returns True if the enough milk."""
    return resources["milk"] >= Menu[type_coffee]["ingredients"]["milk"]

def coffee_enough(type_coffee):
    """returns True if the enough coffee."""
    return resources["coffee"] >= Menu[type_coffee]["ingredients"]["coffee"]

def what_resource_is_needed(type_coffee):
    """returns String of required ingredients."""
    needed = []
    if not water_enough(type_coffee):
        needed.append("water")
    if not milk_enough(type_coffee):
        needed.append("milk")
    if not coffee_enough(type_coffee):
        needed.append("coffee")

    return ", ".join(needed)

def coffee_machine():
    """start the coffee machine."""
    money = 0
    while True:
        ask = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if ask == "report":
            print("Water: {}ml".format(resources["water"]))
            print("Milk: {}ml".format(resources["milk"]))
            print("Coffee: {}g".format(resources["coffee"]))
            print(f"Money: ${money}")

        elif ask == "off":
            break

        elif ask in Menu:

            if water_enough(ask) and milk_enough(ask) and coffee_enough(ask):

                print("Insert your coins: ")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))

                total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

                if total >= Menu[ask]["cost"]:
                    money += Menu[ask]["cost"]

                    change = round(total - Menu[ask]["cost"], 2)
                    if change > 0:
                        print(f"Here is ${change} dollars in change.")

                    #for loop is good here use.
                    resources["water"] -= Menu[ask]["ingredients"]["water"]
                    resources["milk"] -= Menu[ask]["ingredients"]["milk"]
                    resources["coffee"] -= Menu[ask]["ingredients"]["coffee"]

                    print(f"Here is your {ask}. Enjoy!")

                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Sorry there is not enough {what_resource_is_needed(ask)}")

        else:
            print("Invalid input. Please try again.")

coffee_machine()

