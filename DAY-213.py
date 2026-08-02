import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()


def add_student():
    name = input("Enter student name: ")

    # Check if student already exists
    cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
    student = cursor.fetchone()

    if student:
        print("Student already exists!")
        return

    age = int(input("Enter age: "))
    course = input("Enter course: ")

    cursor.execute("""
        INSERT INTO students(name, age, course)
        VALUES (?, ?, ?)
    """, (name, age, course))

    connection.commit()
    print("Student added successfully!")


def search_student():
    value = input("Enter Student Name or ID: ")

    if value.isdigit():
        cursor.execute("SELECT * FROM students WHERE id = ?", (int(value),))
    else:
        cursor.execute("SELECT * FROM students WHERE name = ?", (value,))

    students = cursor.fetchall()

    if students:
        for student in students:
            print("========================")
            print(f"ID      : {student[0]}")
            print(f"Name    : {student[1]}")
            print(f"Age     : {student[2]}")
            print(f"Course  : {student[3]}")
            print("========================")
    else:
        print("Student not found.")


def update_student():
    name = input("Enter student name: ")

    cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    age = int(input("Enter new age: "))
    course = input("Enter new course: ")

    cursor.execute("""
        UPDATE students
        SET age = ?, course = ?
        WHERE name = ?
    """, (age, course, name))

    connection.commit()
    print("Student updated successfully!")


def delete_student():
    name = input("Enter student name: ")

    cursor.execute("DELETE FROM students WHERE name = ?", (name,))

    if cursor.rowcount > 0:
        connection.commit()
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def show_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    for student in students:
        print("=======================")
        print(f"ID      : {student[0]}")
        print(f"Name    : {student[1]}")
        print(f"Age     : {student[2]}")
        print(f"Course  : {student[3]}")
        print("========================")


while True:
    print("""
========== STUDENT MANAGEMENT ==========
1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. Show All Students
6. Exit
========================================
""")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            search_student()

        elif choice == 3:
            update_student()

        elif choice == 4:
            delete_student()

        elif choice == 5:
            show_students()

        elif choice == 6:
            print("Thank you for using the Student Management System!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number.")

connection.close()