numbers = [12, 45, 7, 89, 23, 56, 90]
print(max(numbers))
print(min(numbers))
print(sum(numbers))
numbers_50=[]
for i in numbers :
    if i>50:
        numbers_50.append(i)

print(numbers_50)

student = {
    "Name": "Samarth",
    "Age": 20,
    "Course": "B.Tech AI"
}

print(student.keys())
print(student.values())
student["City"]= "Indore"
student.update({"Age": 21})
print(student)

print(student.items())