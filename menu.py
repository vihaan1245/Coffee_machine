from menuItem import MenuItem

class Menu:
    def __init__(self):
        self.list = [
            MenuItem("Latte", 2.50, 70, 100, 30),
            MenuItem("Espresso", 1.50, 150, 0, 35),
            MenuItem("Cappuccino", 3.00, 150, 100, 40)
        ]

    def get_items(self):
        return '/'.join(item.name for item in self.list)

    def find_drink(self,order_name):
        for item in self.list:
            if item.name.lower() == order_name.lower():
                return item
        print(f"{order_name} not in menu.")
        return None