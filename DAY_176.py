class Student:
    def __init__(self,name,mark):
        self.name = name
        self.__mark=mark
        pass

    def set_marks(self,new_marks):
        if 0< new_marks <100:
            self.__mark=new_marks
            print("Marks Updeted")
        else:
            print("Invalid Marks")

    def get_marks(self):
        print(f"Marks are : {self.__mark}")

    def show_Details(self):
        print(f"Student name : {self.name} \n Marks : {self.__mark}")

student1 = Student("Samarth", 89)

student1.show_Details()

student1.set_marks(95)

student1.show_Details()

student1.set_marks(150)

print(student1.__dict__)

