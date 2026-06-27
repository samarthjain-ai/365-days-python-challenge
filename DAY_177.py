class Vehicel:
    def start(self):
        print("Vehicle Started")

class Car:
    def start(self):
        print("Car Started")

class Bike:
    def start(self):
        print("Bike started")


car = Car()
bike = Bike()

car.start()
bike.start()

vehicles = [Car(), Bike()]

for i  in vehicles:
    i.start()