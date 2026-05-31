# IF-else

Number=int(input("enter a number to check positive or nagative ==>\n"))
if Number<0:
    print("Nagative")
elif Number==0:
    print("Zero")
else:
    print("Positive")


# FOR LOOP
for i in range(1,11):
    print(i*i)

# while loop
n=int(input("Enter a value of n ==> "))
while(n>=1):
    print(n)
    n-=1

# function
def student_result(Marks):
    if Marks>=75:
        print("Distinction")
    elif Marks>=40:
        print("Pass")
    else:
        print("Fail")

student_result(85)


marks = [90, 45, 78, 23, 67, 88]

student_pass=0
student_fail=0
for i in marks:
    if i>=40:
        student_pass+=1
    else:
        student_fail+=1

print("Pass  ==> ",student_pass)
print("Fail  ==> ",student_fail)