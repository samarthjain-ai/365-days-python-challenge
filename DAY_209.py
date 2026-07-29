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


def update_student():
    name = input("Enter a name here : ")

    found = False

    for student in data:
        if student["name"].lower() == name.lower():
            new_age=input("Enter a new age here : ")
            new_course=input("Enter new course here : ")
            student["age"] = new_age
            student["course"] = new_course
            with open("students.json","w") as f:
                j.dump(data,f,indent=4)

            print("Student update successfully")
            found = True
            break

    if not found:
        print("Student not found.")



def delete_student():
    name = input("Enter a name here : ").lower()

    found = False

    for student in data:
        if student["name"].lower() == name.lower():
            data.remove(student)
            with open("students.json", "w") as f:
                j.dump(data, f, indent=4)
            found = True
            print("Student removed")
            break

    if not found:
        print("Student not found.")




def show_students():
    for student in data:
        print(student)


while True:
    menu="""    1 = Enter details 
    2 = search student
    3 = update student
    4 = delete student
    5 = show all students
    6 = Exit 
        """
    print("=== MENU ===")
    print(menu)
    choice = int(input("Enter your choice : "))

    if choice == 1:
        student=user_input()
        for s in data:
            if s["name"].lower() == student["name"].lower():
                print("Student already exists.")
                break
        else:
            data.append(student)
            with open ("students.json","w") as f:
                j.dump(data,f,indent=4)
                print("Student added successfully!")
    elif choice ==2:
        search_student()
    elif choice ==3:
        update_student()
    elif choice==4:
        delete_student()
    elif choice ==5:
        show_students()
    elif choice ==6 :
        print("Thank you for using")
        break


