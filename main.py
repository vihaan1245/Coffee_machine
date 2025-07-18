from makeCoffee import CoffeeMaker
from menu import Menu
from moneyMachine import moneyMachine

money_machine = moneyMachine()
make_coffee = CoffeeMaker()
menus = Menu()

is_on = True

while is_on:
    choice = input(f"What would you like {menus.get_items()}?")

    if choice == "off":
        print("Turning off the coffee machine....")
        is_on = False

    elif choice == "report":
        make_coffee.report()
        money_machine.report()

    else:
        drink = menus.find_drink(choice)
        if make_coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            make_coffee.make_coffee(drink)

