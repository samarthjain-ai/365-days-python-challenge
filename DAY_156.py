students = {
    "Samarth": 90,
    "Riya": 78,
    "Bob": 45,
    "John": 30
}

for student in students:
    print(f"{student} --> {students[student]}")

print("Highest marks ==> ",max(students.values()))
print("Lowest  marks ==> ",min(students.values()))

count_pass=0
count_fail=0

for student in students:
    if students[student]>40:
        count_pass+=1
    else:
        count_fail+=1

print("Pass students are ==> ",count_pass)
print("Fail students are ==> ",count_fail)


def grade(marks):
    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 35:
        return "D"

    else:
        return "FAIL"
    
for  student in students:
    result = grade(students[student])
    print(f"{student} status ==> {result}")