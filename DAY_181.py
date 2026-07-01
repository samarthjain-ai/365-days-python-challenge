class Animal:

    def move(self):
        print("Animal moves")

class Bird(Animal):

    def move(self):
        print("Bird Fly")

animals = [Animal(), Bird()]

for animal in animals:
    animal.move()