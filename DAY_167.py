
class Student:
    total_student=0
    def __init__(self,name,age,mark,section,roll_no):
        
        self.name=name
        self.age=age
        self.mark=mark
        self.section=section
        self.rool_no=roll_no
        Student.total_student+=1
        print("Student created : ",Student.total_student)
        pass
    def show_details(self):
        print(f"Student {self.rool_no} Details")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Mark : {self.mark}")
        print(f"Section : {self.section}")
        print(f"Roll_no : {self.rool_no}")
        pass

    def birthday(self):
        self.age = self.age+1
        pass

    def update_marks(self,new_marks):
        if self.mark != new_marks:
            self.mark = new_marks
        else:
            print(f"Same marks")
        pass
    def calculate_grade(self):
        if 90<=self.mark <=100:
            print("A")
        elif self.mark >=80:
            print("B")
        elif self.mark >=70:
            print("C")
        elif self.mark >=40:
            print("D")
        elif self.mark>=0:
            print("F")
        else:
            print("Invalid marks")
        pass

    def check_pass_fail(self):
        if self.mark>=40:
            print("PASS")
        else:
            print("FAIL")
        pass
    def change_section(self,new_section):
        if self.section !=  new_section:
            self.section = new_section
        pass
        

student1 = Student("Samarth",18,89,"B","001")
student2 = Student("Bob",14,56,"A","002")
student3 = Student("Jhon",23,90,"C","003")

student1.birthday()
student1.update_marks(90)
student1.calculate_grade()
student1.change_section("A")
student1.check_pass_fail()
student1.show_details()

student2.birthday()
student2.update_marks(97)
student2.calculate_grade()
student2.change_section("D")
student2.check_pass_fail()
student2.show_details()

student3.birthday()
student3.update_marks(80)
student3.calculate_grade()
student3.change_section("B")
student3.check_pass_fail()
student3.show_details()

