class Student:
    def __init__(self,name,mark,course):
        self.name=name
        self.mark=mark
        self.course=course
        pass


    def __str__(self):
        return f"student : {self.name} \nMark : {self.mark}  \nCourse : {self.course}"

student1 =Student("Samarth",98,"B.Tech AI/ML")
print(student1)