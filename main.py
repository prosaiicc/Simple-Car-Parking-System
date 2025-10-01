from Car import Car
from Park_system import ParkingSystem
from money_machine import MoneyMachine

run = True

money = MoneyMachine()
parkingSystem = ParkingSystem()


while run:

    print("Welcome to the Parking !")
    ch = input("Would you like to Park or take a car? : ")

    if ch.lower() == "off":
        break
    elif ch.lower() == "report":
        parkingSystem.report()
    elif ch.lower() == "park":
        if parkingSystem.checkSufficient():

            plate = input("Enter car plate : ").lower()
            stay = input("What program do you want (overnight/monthly) : ")
            if stay.lower() == "overnight":
                day = int(input("For how many days do you plan on parking the car? : "))
                car = Car(plate, stay)
                car.days = day
                if money.make_payment(car):
                    parkingSystem.ParkCar(car)
            elif stay.lower() == "monthly":
                month = int(input("For how many months do you plan on parking the car? : "))
                car = Car(plate, stay)
                car.months = month
                if money.make_payment(car) :
                    parkingSystem.ParkCar(car)



            else :
                print("Not an available program!")



        else :
            print("There is not enough parking space!")


    elif ch.lower() == "take":
        plate = input("Enter car plate : ").lower()
        stay = input("What program do you want (overnight/monthly) : ").lower()

        parkingSystem.DeparkCar(plate,stay)



