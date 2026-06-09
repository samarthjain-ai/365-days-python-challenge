numbers = [12, 45, 67, 89, 23, 56, 90]
print(max(numbers))
print(min(numbers))
print(sum(numbers)/len(numbers))

count_g=0
count_l=0

for number in numbers:
    if number>50:
        count_g+=1
    else:
        count_l+=1
print(count_g)
print(count_l)