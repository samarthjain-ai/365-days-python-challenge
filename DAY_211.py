import sqlite3

connection = sqlite3.connect(("students.db"))

cursor = connection.cursor()

def search_student():
    name=input("Enter name : ")

    cursor.execute("""SELECT * FROM students WHERE Name =? """,(name,))
    students = cursor.fetchall()
    for student in students:
        print(student)
    connection.commit()

def update_student():
    name=input("Whose age to change : ")
    age =int(input("Enter your age "))
    cursor.execute("""UPDATE students 
    SET Age = ? 
    WHERE Name=?""",(age,name))
    connection.commit()

def delete_student():
    name=input("Enter the name : ")
    cursor.execute("""DELETE FROM students WHERE Name =?""",(name,))
    connection.commit()

connection.commit()


while True:
    menu="""1-search student
    2-update student
    3-delete studet
    4-Exit"""
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