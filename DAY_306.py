numbers = [12, 45, 23, 45, 67, 12, 89, 67]

largest = numbers[0]
second_largest=0
for j in numbers:
    if largest <=j:
        second_largest=largest
        largest = j

print(second_largest)
print(largest)