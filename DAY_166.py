# Time to deep dive in oops start from today 

class Student:
    def __init__(self,student,age,mark):
        self.name=student
        self.age=age
        self.mark=mark
        pass

    def show(self):
        print(f"{self.name} is {self.age} years old and get {self.mark} mark")

    pass

student1 = Student("samarth",18,89)
student2 = Student("Bob",45,78)

student1.show()
student2.show()