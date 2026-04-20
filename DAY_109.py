# Doning small work because of less time

# Question 1- Smart Number Analyzer

n = int(input("Enter a number to analyzes it "))

if n <0:
    if n%2==0:
        print("Negative even")
    else:
        print("Negative odd")
elif n==0:
    print("ZERO")
else:
    if n%2==0:
        print("Positive even")
    else:
        print("Positive odd")

# Question 2 - Advanced Grade System 
mark = int(input("Enter your mark 0-100  "))

if 0<=mark<=100:
    if mark >=90:
        print ("A+")
    elif mark>=80:
        print ("A")
    elif mark>=70:
        print("B")
    elif mark>=60:
        print("C")
    elif mark >=50:
        print("D")
    else:
        print("FAIL")
else:
    print("INVALI NUMBER")

#Question 3 Login System (Basic)

username = "samarth jain"
password = "1234"
enter_username=input("Enter a username ")
enter_password = input("Enter a password")
if enter_username==username:
    if enter_password==password:
        print("Login Successful")
    else:
        print("Invalid password")
else:
    print("User not found")
    
