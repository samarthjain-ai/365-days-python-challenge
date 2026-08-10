def calculator():
    try:
        a= float(input("Enter your first number : "))
        o=input("Enter operater : ") 
        b=float(input("Enter your second number : ")) 
        if o == "+":
            print(a + b)
        elif o == "-":
            print(a - b)
        elif o == "*":
            print(a * b)
        elif o == "/":
            print(a / b)
        else:
            print("Invalid operator")

    except ValueError:
        print("Please enter a valid number ")

    except ZeroDivisionError:
        print("Cannot divide by Zero")

    else:
        print("Calculation completed successfully")

    finally:
        print("Calculator operation finished")

while True:
    menu="""    1-calculator
    2-Exit"""
    print(menu)
    chiose=int(input("Enter you choise : "))

    try:

        if chiose==1:
            calculator()
        elif chiose==2:
            break
        else:
            print("PLZ enter a valid chiose")
    except ValueError:
        print("Enter a number")