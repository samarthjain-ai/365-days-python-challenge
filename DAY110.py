# student mask table
import sqlite3
conn = sqlite3.connect("mark_table.db")
cursor =conn.cursor()

cursor.execute(""" CREATE TABLE student_marks (
               name text,
               mark INTEGER ,
               subject text
               )
""")
print ("table created")

data= [("samarth",89,"ce"),("subh",78,"daup"),("ram",34,"la")]
cursor.executemany("INSERT INTO student_marks VALUES (?,?,?)", data)
print("DATA inserted")

cursor.execute("SELECT rowid,* FROM student_marks")
details = cursor.fetchall()
for detail in details:
    print(detail)

conn.commit()
conn.close()