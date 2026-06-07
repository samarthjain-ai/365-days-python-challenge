# Question 1
text = "Artificial Intelligence"

print("Total number of characters ==> ",len(text))
print("Convert to uppercase ==> ",text.upper())
print("Convert to lowercase ==> ",text.lower())

count=0
for l in text:
    if l == "i":
        count+=1
print(count)
print(text[::-1])

# Question 2
numbers = [12, 45, 7, 89, 23, 56, 90, 45]
N=set(numbers)
print(N)

numbers_updated =list(N)
print(numbers_updated)

print(numbers_updated[::-1])
print(numbers_updated[-2])

# Question 3
names = ["Samarth", "Riya", "Bob", "John"]

for i in names:
    print(f"Hello {i}")

# Question 4
def vowel_count(text):
    vowel=0
    for i in text:
        if i in "AEIOUaeiou":
            vowel+=1
    print(vowel)

vowel_count("samarth")
 