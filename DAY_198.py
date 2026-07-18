class Circle:
    PI=3.14
    def __init__(self,radius):
        self.radius=radius
        pass
    def area(self):
        return Circle.PI*self.radius*self.radius
    def circumference(self):
        return 2*Circle.PI*self.radius

circle1 = Circle(7)

print(f"Area : {circle1.area()}")
print(f"circumference : {circle1.circumference()}")
