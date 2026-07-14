class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        pass
    def area(self):
        return f"Area : {self.length*self.width}"
    
    def perimeter(self):
        return f"perimeter : {2*(self.length+self.width)}"

rect = Rectangle(10, 5)
print(rect.area())
print(rect.perimeter())