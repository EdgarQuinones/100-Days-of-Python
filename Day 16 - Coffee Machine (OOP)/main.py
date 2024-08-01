from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


def get_coffee(coffee_type):
    """Uses the new classes to handle the coffee machine in a much
    more efficient way compared to day 15"""
    coffee = menu.find_drink(coffee_type)
    if coffee != "None":
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    users_input = input(f"What would you like? {menu.get_items()}: ")

    if users_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif users_input == "off":
        print("Coffee Machine Powering Off.")
        machine_on = False
    else:
        get_coffee(users_input)
