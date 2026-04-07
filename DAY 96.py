#DAY 96 

#Q1 - prime number

number = int(input("Enter your number here ==> "))

if number>1:
    for num in range(2,number):
        if number%num==0:
            print("IT IS NOT A PRIME NUMBER")
            break
    else:
        print("IT IS A PRIME NUMBER")
else:
    print("NOT A PRIME NUMBER")

#Q2 - Fibonacci series

num= int(input("Enter you number "))
a=0
b=1

if num>1:
    print(a,end=" ")
if num>2:
    print(b,end=" ")
for i in range(2,num):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

#Q3 - character Frequency 

words = input(f"Enter your words here ")
freq= {}

for char in words:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] =1

for key,value in freq.items():
    print(key,":",value)