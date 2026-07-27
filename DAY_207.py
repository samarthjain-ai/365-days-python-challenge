import json as j

def user_input():
    name= input("Enter your name here : ")
    age = input("Enter your age :")
    course = input("Enter your course : ")
    student = {
    "name": name,
    "age": age,
    "course": course
    }
    return student

with open ("students.json","r") as f:
    data =j.load(f)
    print(data)


def search_student():
    name = input("Enter a name here : ")

    found = False

    for student in data:
        if student["name"].lower() == name.lower():
            print("Student Found!")
            print(student)
            found = True
            break

    if not found:
        print("Student not found.")



while True:
    menu="""    1 = Enter details 
    2 = search student
    3 = Exit 
        """
    print("=== MENU ===")
    print(menu)
    choice = int(input("Enter your choice : "))

    if choice == 1:
        student=user_input()
        data.append(student)
        with open ("students.json","w") as f:
            j.dump(data,f,indent=4)
        print("Student added successfully!")
    elif choice ==2:
        search_student()
    
    elif choice ==3 :
        print("Thank you for using")
        break


