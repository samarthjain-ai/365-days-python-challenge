import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

cursor.execute(""" 
INSERT INTO students(name,age,course)
VALUES(?,?,?)""",("samarth",24,"B.Tech AI"))

cursor.execute("SELECT* FROM students")
students=cursor.fetchall()
for student in students:
    for student in students:
        print(f"""
        ID      : {student[0]}
        Name    : {student[1]}
        Age     : {student[2]}
        Course  : {student[3]}
        ----------------------
        """)

connection.commit()

print("Table created successfully!")

connection.close()