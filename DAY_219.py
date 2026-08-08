import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS company (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    salary INTEGER,
    city TEXT
)
""")

def insert_data():
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    salary = int(input("Enter your salary: "))
    city = input("Enter your city: ")

    cursor.execute("""
        INSERT INTO company (name, department, salary, city)
        VALUES (?, ?, ?, ?)
    """, (name, department, salary, city))

    connection.commit()
    print("Employee added successfully!")


# Q1 
def show_details():
    cursor.execute("SELECT * FROM company")

    employees = cursor.fetchall()

    for employee in employees:
        print(employee)


# Q2
def search_emp_dept():
    department = input("Enter department: ")

    cursor.execute("""
        SELECT * FROM company
        WHERE department = ?
    """, (department,))

    employees = cursor.fetchall()

    for employee in employees:
        print(employee)


def emp_40000():
    cursor.execute("""
        SELECT * FROM company
        WHERE salary > 40000
    """)

    employees = cursor.fetchall()

    for employee in employees:
        print(employee)


def emp_high_low():
    cursor.execute("""
        SELECT * FROM company
        ORDER BY salary DESC
    """)

    employees = cursor.fetchall()

    for employee in employees:
        print(employee)


def top_three():
    cursor.execute("""
        SELECT * FROM company
        ORDER BY salary DESC
        LIMIT 3
    """)

    employees = cursor.fetchall()

    for employee in employees:
        print(employee)


def different_departments():
    cursor.execute("""
        SELECT DISTINCT department
        FROM company
    """)

    departments = cursor.fetchall()

    for department in departments:
        print(department[0])


def search_letter():
    cursor.execute("""
        SELECT * FROM company
        WHERE name LIKE ?
    """, ("S%",))

    employees = cursor.fetchall()

    for employee in employees:
        print(employee)

def total_count():
    cursor.execute("""
        SELECT COUNT(*)
        FROM company
    """)

    total = cursor.fetchone()

    print("Total Employees:", total[0])


# ---------------- MENU ----------------

while True:

    menu = """
    ===== COMPANY DATABASE =====

    1 - Add Employee
    2 - Show All Employees
    3 - Show Employees by Department
    4 - Employees with Salary > 40000
    5 - Sort Employees by Salary
    6 - Top 3 Highest-Paid Employees
    7 - Show Different Departments
    8 - Names Starting with S
    9 - Total Employees
    10 - Exit
    """

    print(menu)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_data()

    elif choice == 2:
        show_details()

    elif choice == 3:
        search_emp_dept()

    elif choice == 4:
        emp_40000()

    elif choice == 5:
        emp_high_low()

    elif choice == 6:
        top_three()

    elif choice == 7:
        different_departments()

    elif choice == 8:
        search_letter()

    elif choice == 9:
        total_count()

    elif choice == 10:
        print("Thank you for using the program")
        break

    else:
        print("Invalid choice ")


connection.close()