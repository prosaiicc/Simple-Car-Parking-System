class MoneyMachine:

    def __init__(self):
        self.money_received = 0

    COIN_VALUE = {
        "enaeura" : 1.0,
        "dieura" : 2.0,
    }

    PROGRAMS = {
        "monthly" : 120.0,
        "overnight" : 12.0
    }

    CURRENCY = "€"

    #Returns Profit
    def report(self):
        return self.money_received

    #coin machine operation

    def process_coins(self):
        #Returns coins received
        print("Please insert coins.")
        for coin in self.COIN_VALUE:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUE[coin]
        return self.money_received

    def find_cost(self,obj):
        program = obj.program.lower()
        if program == "overnight":
            cost = int(self.PROGRAMS[program]) * obj.days
        elif program == "monthly":
            cost = int(self.PROGRAMS[program]) * obj.months
        return cost

    def make_payment(self,obj):
        #Returns true if payment is successful
        self.process_coins()
        cost = self.find_cost(obj)

        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.money_received += cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

