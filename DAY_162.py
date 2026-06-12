numbers = [15, 10, 37, 48, 59, 63, 71]
print("Sum ==> ",sum(numbers))

Even_count=0
Odd_count=0
for i in numbers:
    if i%2==0:
        Even_count+=0
    else:
        Odd_count==1
print("Even count ==> ",Even_count)
print("Odd  count  ==> ",Odd_count)

largest=numbers[0]
smallest=numbers[0]
for i in numbers:
    if i >= largest:
        largest=i
    if i<smallest:
        smallest=i
print(largest)
print(smallest)

students = {
    "Samarth": 90,
    "Riya": 78,
    "Bob": 45,
    "John": 34
}

print(students.items())
print(students.values())

print(max(students.values()))
print(min(students.values()))