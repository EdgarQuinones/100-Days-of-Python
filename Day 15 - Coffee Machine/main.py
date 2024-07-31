# Today I made a coffee machine. It contains 3 flavors, along with their ingredients.
# It contains the price for each. The program will keep track of how many ingredients left,
# along with total profit made. It ends once the user "turns off" the machine.
# It will not allow purchases without enough money, and gives change back.

from menu import MENU
from resources import coffee_resources


def print_report():
    """Prints total ingredients remaining, along with total profit."""
    
    print(f"Water : {coffee_resources["water"]}ml")
    print(f"Milk : {coffee_resources["milk"]}ml")
    print(f"Coffee : {coffee_resources["coffee"]}g")
    print(f"Money : ${profit}")


def enough_money(coffee_type):
    """Tells the user how much is owed, and gives change back
    if proper amount of money is paid. Otherwise, coffee is not given."""
    
    price_of_coffee = MENU[coffee_type]["cost"]
    print(f"{coffee_type}s costs ${price_of_coffee}")
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    quarters_total = quarters * .25
    dimes_total = dimes * .10
    nickles_total = nickles * .05
    pennies_total = pennies * .01
    payment = quarters_total + dimes_total + nickles_total + pennies_total

    if payment >= price_of_coffee:
        global profit
        profit += price_of_coffee

        change = "%.2f" % round(payment - price_of_coffee, 2)
        if float(change) > 0:
            print(f"Here is ${change} in change.")

        print(f"Here is your {coffee_type}, Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(water_required, milk_required, coffee_required):
    """Removes ingredients used to make the coffee."""
    
    coffee_resources["water"] -= water_required
    coffee_resources["milk"] -= milk_required
    coffee_resources["coffee"] -= coffee_required


def get_coffee(coffee_type):
    """Gets coffee type user chooses and checks if there are enough
    resources, otherwise will prompt user again."""
    
    milk_required = 0
    if coffee_type != "espresso":
        milk_required = MENU[coffee_type]["ingredients"]["milk"]
    water_required = MENU[coffee_type]["ingredients"]["water"]
    coffee_required = MENU[coffee_type]["ingredients"]["coffee"]

    water_remaining = coffee_resources["water"]
    milk_remaining = coffee_resources["milk"]
    coffee_remaining = coffee_resources["coffee"]

    enough_resources = True
    if water_remaining < water_required:
        print("Sorry there is not enough water.")
        enough_resources = False
    if milk_remaining < milk_required:
        print("Sorry there is not enough milk.")
        enough_resources = False
    if coffee_remaining < coffee_required:
        print("Sorry there is not enough coffee.")
        enough_resources = False

    if enough_resources and enough_money(coffee_type):
        make_coffee(water_required, milk_required, coffee_required)
            

profit = 0
machine_on = True
while machine_on:
    users_input = input("What would you like? (espresso/latte/cappuccino): ")

    if users_input == "report":
        print_report()
    elif users_input == "off":
        print("Coffee Machine Powering Off.")
        machine_on = False
    else:
        get_coffee(users_input)
