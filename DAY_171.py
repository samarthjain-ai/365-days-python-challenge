class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("Samarth")
student2 = Student("Bob")

print(student1.name)
print(student2.name)


class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("Samarth")
student2 = Student("Bob")

student1.name = "Alex"

print(student1.name)
print(student2.name)