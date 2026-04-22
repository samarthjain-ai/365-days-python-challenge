## student mask table
import sqlite3
conn = sqlite3.connect("mark_table.db")
cursor =conn.cursor()


cursor.execute("DELETE FROM student_marks WHERE rowid = 3 ")

cursor.execute("SELECT rowid,* FROM student_marks")
details = cursor.fetchall()
for detail in details:
    print(detail)

conn.commit()
conn.close()