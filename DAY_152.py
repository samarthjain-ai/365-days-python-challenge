marks = [90, 45, 78, 23, 67, 88]
print(max(marks))
print(min(marks))
print(sum(marks)/len(marks))

count=0

for i in marks:
    if i>60:
        count+=1

print(count)

student = {
    "Name":"Samarth",
    "Department":"AI",
    "Marks":90
}

print(student.keys())
print(student.values())
student["Marks"]=95
print(student.values())

def calculate_grade(marks):
    if marks>=90:
        print("A")
    elif marks>=75:
        print("B")
    elif marks >=60:
        print("C")
    elif marks>=35:
        print("D")
    else:
        print("F")
    
calculate_grade(90)
calculate_grade(72)
calculate_grade(56)
calculate_grade(32)
