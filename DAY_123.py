# light practice
# Question 1 — Smart Electricity Bill

def calculate_bill(units):
    if 0<=units<=100:
        return 5*units
    elif 101<=units<=200:
        return 7*units
    else:
        return 10*units

units=int(input("Enter your unit here to calculate  the bill ==>  \n"))
print("Bill ==> ",calculate_bill(units))


# Question 2 - Number mood analyzer

def analyze_number(n):
    if n<0:
        print("Negative")
        if n%2==0:
            print("Negative Even")
            if n%5==0:
                print("divisibal by five")
            else:
                print("Not divisible by 5")
        else:
            print("Negative Odd")
            if n%5==0:
                print("divisibal by five")
            else:
                print("Not divisible by 5")
    elif n==0:
        print("Zero")
        print("NOT divisibal by 5")
    else:
        print("positive")
        if n%2==0:
            print("Positive Even")
            if n%5==0:
                print("divisibal by five")
            else:
                print("Not divisible by 5")
        else:
            print("postive Odd")
            if n%5==0:
                print("divisibal by five")
            else:
                print("Not divisible by 5")
        

n=int(input("Enter your number here"))
analyze_number(n)

# Question 3 - mini login + otp system


def login_system(u,p):

    username="samarth"
    password ="1234"
    otp = 5678
    if u==username:
        if p==password:
            print("Login Successful")
        else:
            print("Wrong password")
            print("Try by OTP")
            o=int(input("Enter OTP ==> "))
            if o==otp:
                print("Login by OTP")
            else:
                print("Wrong OTP")
    else:
        print("User name not found")

u=str(input("Enter username   ==>  ")).lower()
p=input("Enter password here  ==> ")

login_system(u,p)