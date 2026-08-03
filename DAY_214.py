import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students ORDER BY name")
print(cursor.fetchall())

cursor.execute("SELECT * FROM students LIMIT 1")
print(cursor.fetchall())

connection.close()