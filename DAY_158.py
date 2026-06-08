marks = [78, 45, 90, 67, 34, 88, 56]
print(max(marks))
print(min(marks))
print(sum(marks)/len(marks))
count=0
for mark in marks:
    if mark>60:
        count+=1
print(count)

students = {
    "Samarth": 90,
    "Riya": 78,
    "Bob": 45,
    "John": 34
}

print(students.keys())
print(students.values())
print(max(students.values()))

