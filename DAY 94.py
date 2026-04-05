#DAY 94
#Q1
E= int(input("Enter a value to reverse "))
print("Reverse using list identity ",str(E)[::-1])

rev = 0
while E>0:
    digit = E%10
    rev = rev*10 +digit
    E = E // 10
print("Reverse using loop ==> ",rev)

#Q2
list_1=[1,2,3,4,5,9]
print("MAX NUMBER useing max Function ==> ", max(list_1))
largest=list_1[0]
for i in list_1:
    if i > largest:
        largest = i

print("Largest number using loop ==> ",largest)

#Q3
sentance = input("Enter your sentence here ==> ")
count_v=0
for char in sentance:
    if char in "AEIOUaeiou":
        count_v+=1
        
print("Vowels count ==> ",count_v)
