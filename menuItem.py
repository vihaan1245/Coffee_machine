class MenuItem:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name  # Name of the drink
        self.cost = cost
        self.ingredients = {"Water":water, "Milk":milk, "Coffee":coffee}  # Dictionary of ingredients and their quantities

    def __repr__(self):
        return f"Name: {self.name}, Ingredients: {self.ingredients}, Cost: ${self.cost}"


