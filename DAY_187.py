class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        pass

    def __eq__(self, value):
        return self.name==value.name and self.marks==value.marks


student1 = Student("Samarth", 98)
student2 = Student("Samarth", 98)
student3 = Student("Alex", 90)
print(student1 == student2)
print(student1 == student3)

class  Wallet:
    def __init__(self,money):
        self.money=money
        pass
    def __add__(self, other):
        return self.money+other.money
        
wallet1 = Wallet(500)
wallet2 = Wallet(1000)
wallet3 = Wallet(250)

print(wallet1 + wallet2 + wallet3)
