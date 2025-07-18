class moneyMachine:
    CURRENCY = "$"
    coin_values = {
        "Quarters":0.25,
        "Dimes":0.10,
        "Nickels":0.05,
        "Pennies":0.01
    }
    def __init__(self):
        self.profit = 0.0
        self.money_received = 0.0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def make_payment(self,cost):
        print(f"The cost is ${cost}. Please insert coins.")
        for coin in self.coin_values:
            self.money_received += int(input(f"How many {coin}?"))*self.coin_values[coin]
        if self.money_received < cost:
            print("Sorry there is not enough money, the money has been refunded.")
            self.money_received = 0.0
            return False
        else:
            change = round(self.money_received - cost, 2)
            print(f"Here is your {self.CURRENCY}{change}!")
            self.profit += cost
            self.money_received = 0.0
            return True
