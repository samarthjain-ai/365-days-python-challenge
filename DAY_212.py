import sqlite3

connection = sqlite3.connect(("students.db"))

cursor = connection.cursor()

def search_student():
    name=input("Enter name OR id  : ")

    cursor.execute("""SELECT * FROM students WHERE Name =? OR id =? """,(name,name))
    students = cursor.fetchall()
    for student in students:
        print("========================")
    print(f"ID      : {student[0]}")
    print(f"Name    : {student[1]}")
    print(f"Age     : {student[2]}")
    print(f"Course  : {student[3]}")
    print("========================")

    connection.commit()

def update_student():
    
    name=input("Whose age to change : ")
    age =int(input("Enter your age "))
    cursor.execute("""UPDATE students 
    SET Age = ? 
    WHERE Name=?""",(age,name))
    connection.commit()
    if cursor.rowcount > 0:
        print("Student Updated Successfully!")
    else:
        print("Student Not Found!")

def delete_student():
    name=input("Enter the name : ")
    cursor.execute("""DELETE FROM students WHERE Name =?""",(name,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

while True:
    menu="""1-search student
    2-update student
    3-delete studet
    4-Exit"""
    print(menu)
    choise=int(input("Enter your choise : "))
    if choise==1:
        search_student()
    elif choise==2:
        update_student()
    elif choise==3:
        delete_student()
    elif choise==4:
        break
connection.close()