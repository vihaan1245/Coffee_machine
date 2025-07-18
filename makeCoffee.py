from importlib.resources import is_resource

import menuItem

class CoffeeMaker:
    def __init__(self):
        self.resources = {"Water": 1000, "Milk": 900, "Coffee": 500}  # Initial resources

    def report(self):
        for resource in self.resources:
            print(f"The amount of {resource} is {self.resources[resource]}ml.")

    def is_resource_sufficient(self,drink:menuItem):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough of {item}")
                return False
        return True

    def make_coffee(self,order:menuItem):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}!")

