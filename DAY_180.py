class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name):
        super().__init__(name)


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

student1 = Student("Samarth")
teacher1 = Teacher("Bob")
student2 = Student("Alex")

people = [student1, teacher1, student2]

for person in people:

    print(f"Name : {person.name}")

    if isinstance(person, Student):
        print("Student Found")

    elif isinstance(person, Teacher):
        print("Teacher Found")

    print("-" * 20)