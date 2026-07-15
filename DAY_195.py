class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        Car.total_car += 1

    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")

    @classmethod
    def show_total_cars(cls):
        print(f"Total Cars : {cls.total_car}")


car1 = Car("Toyota", "Fortuner")
car2 = Car("BMW", "X5")
car3 = Car("Tesla", "Model 3")

car1.show_details()
car2.show_details()
car3.show_details()

Car.show_total_cars()