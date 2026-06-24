class Person:
    def __init__(self,name):
        self.name=name
        pass

    def introduce(self):
        print(f"Hello myself {self.name}")

class Student(Person):
    def __init__(self,name,course):
        super().__init__(name)
        self.course=course
        pass

    def introduce(self):
        print(f"Hello myself {self.name} i was inrolled in {self.course}")
        super().introduce()

P1=Student("samarth","B.Tech")
P1.introduce()