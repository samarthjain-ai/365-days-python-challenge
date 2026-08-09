import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
department TEXT , 
salary INTEGER,
city TEXT )
""")

def insert_emp():
    name = input("Enter name : ")
    department = input("Enter department :  ")
    salary = int(input("Enter salary :  "))
    city = input("Enter city :  ")

    cursor.execute("""INSERT INTO employees
      (name,department,salary,city)
      VALUES(?,?,?,?)""",(name,department,salary,city))
    
    connection.commit()
    print("Employee added successfully!")

# Q1
def show_all():
    cursor.execute("SELECT * FROM employees")
    emps=cursor.fetchall()
    for emp in emps:
        print(emp)

# Q2
def emp_AI():
    cursor.execute("""SELECT *FROM employees WHERE LOWER(department) = ?""",("ai",))
    emps=cursor.fetchall()
    for emp in emps:
        print(emp)

# Q3
def emp_50000():
    cursor.execute("""SELECT * FROM employees WHERE salary > 50000""")
    emps=cursor.fetchall()
    for emp in emps:
        print(emp)
# Q4
def emp_high_low():
    cursor.execute("""SELECT * FROM employees ORDER BY salary DESC""")
    emps=cursor.fetchall()
    for emp in emps:
        print(emp)
# Q5
def emp_Top_3():
    cursor.execute("""SELECT *FROM employees ORDER BY salary DESC LIMIT 3""")
    emps=cursor.fetchall()
    for emp in emps:
        print(emp)
# Q6
def emp_Unique():
    cursor.execute("""
        SELECT DISTINCT department
        FROM employees """)
    departments = cursor.fetchall()
    for department in departments:
        print(department[0])
# Q7
def emp_name_s():
    cursor.execute("""SELECT * FROM employees WHERE name LIKE ? """,("S%",))
    emps=cursor.fetchall()
    for emp in emps:
        print(emp)
# Q8
def count_emp():
    cursor.execute("""SELECT COUNT(*) FROM employees""")
    emps=cursor.fetchall()
    for emp in emps:
        print(emp)
# Q9 
def search_emp():
    name = input("Enter employee name: ")

    cursor.execute("""
        UPDATE employees
        SET salary = ?
        WHERE name = ?
    """, (75000, name))

    connection.commit()

    if cursor.rowcount > 0:
        print("Salary updated successfully!")
    else:
        print("Employee not found.")

# Q10
def delete_emp():
    name = input("enter your name here : ")
    cursor.execute("""DELETE FROM employees WHERE name =?""",(name,))
    connection.commit()


while True:

    menu = """
===== COMPANY DATABASE =====

1 - Add Employee
2 - Display employees who work in the AI department
3 - Display employees whose salary is greater than 50,000
4 - Display all employees from highest salary to lowest salary
5 - Display the 3 highest-paid employees
6 - Display all unique departments
7 - Find employees whose name starts with S
8 - Find the total number of employees
9 - Update the salary of one employee
10 - Delete one employee
11 - EXIT
"""

    print(menu)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_emp()

    elif choice == 2:
        emp_AI()

    elif choice == 3:
        emp_50000()

    elif choice == 4:
        emp_high_low()

    elif choice == 5:
        emp_Top_3()

    elif choice == 6:
        emp_Unique()

    elif choice == 7:
        emp_name_s()

    elif choice == 8:
        count_emp()

    elif choice == 9:
        search_emp()

    elif choice == 10:
        delete_emp()

    elif choice == 11:
        print("Thank you for using the program")
        break

    else:
        print("Invalid choice!")