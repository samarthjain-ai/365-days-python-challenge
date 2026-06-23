class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_animal(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def show_dog(self):
        print(f"Breed: {self.breed}")



dog1 = Dog("Dog", 3, "i donot know any breed")
dog1.show_animal()  
dog1.show_dog()     
