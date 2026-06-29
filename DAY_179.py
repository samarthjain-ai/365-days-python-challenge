class Dog:
    def speak(self):
        print("Dog says Bhoo Bhoo")


class Robot:
    def speak(self):
        print("Robot says Hello Human")


class Teacher:
    def speak(self):
        print("Teacher says Welcome Students")


class Alien:
    def speak(self):
        print("Alien says Unknown Language")

def make_speak(obj):
    obj.speak()

dog = Dog()
robot = Robot()
teacher = Teacher()
alien = Alien()

print("----- Calling Individually -----")

make_speak(dog)
make_speak(robot)
make_speak(teacher)
make_speak(alien)

objects = [Dog(),Robot(),Teacher(),Alien()]

print("\n----- Calling Using Loop -----")

for obj in objects:
    make_speak(obj)