class Animal:

    def __init__(self,name):
        self.name=name
        pass

    def eat(self):
        print(f"{self.name} is Eating")
    def sleep(self):
        print(f"{self.name} is sleep")
    
class Dog(Animal):

    def bark(self):
        print(f"{self.name} say Bhoo bhoo")

dog=Dog("DOG")

dog.eat()
dog.sleep()
dog.bark()

    