from Car import Car
from money_machine import MoneyMachine
class ParkingSystem:

    def __init__(self):
        self.theseis = 5
        self.history = []
        self.overnight = []
        self.monthly = []



    def report(self):
        """Prints a report of the parking"""

        money = MoneyMachine()
        print("Report: ")
        print(f"The parking has still {self.theseis} parking spaces left. ")
        print(f"The number of the cars that stay overnight are {len(self.overnight)}. ")
        print(f"The number of the cars that stay monthly are {len(self.monthly)}. ")

    def checkSufficient(self):
        """Checks if there is enough parking space"""
        if self.theseis >= 1:
            return True
        else :
            return False


    def ParkCar(self,obj):
        """Parks the car into a parkking space"""
        if obj.program.lower() == "overnight":
            self.overnight.append(obj)
            self.history.append(obj)
            self.theseis -= 1
            print("You have successfully parked the car!")

        elif obj.program.lower() == "monthly":
            self.monthly.append(obj)
            self.history.append(obj)
            self.theseis -= 1
            print("You have successfully parked the car!")
        else :
            print("That is not an available program. Your settings has been reset!")




    def DeparkCar(self,plate,program):
        """Takes out the car from a parking space"""
        if program == "overnight":

            for car in self.overnight:
                if car.am == plate :
                    self.overnight.remove(car)
                    self.theseis += 1
                    print("Thank you for choosing us!")

        elif program == "monthly" :
            for car in self.monthly:
                if car.am == plate:
                    self.monthly.remove(car)
                    self.theseis += 1
                print("Thank you for choosing us!")
        else :
            print("Wrong plate!")






