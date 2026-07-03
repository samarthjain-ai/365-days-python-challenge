from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        print("Every child must implement me") 

class Dog(Animal):
    def sound(self):
        print("Dog says Bhoo Bhoo")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow")
    

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

    





























   
