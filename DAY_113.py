# Euclid Algorithm 
a = int(input("ENter a "))
b = int(input("Enter b "))

while b!=0:
    temp=b
    b=a%b
    a=temp
print(a)

# TASK - 1 update the stuednt marks
import sqlite3 
conn = sqlite3.connect("mark_table.db")
cursor = conn.cursor()
update_mark=[34]
id =[2]
cursor.execute("UPDATE student_marks SET mark = '65' WHERE rowid ='2' ")

cursor.execute("SELECT rowid, * FROM student_marks ")
items = cursor.fetchall()
for item in items:
    print(item)

print("\n")

# TASK - Filter sshow only with marks > 50
print("STUDENT WITH 50+ MARKS \n")
cursor.execute("SELECT * FROM student_marks WHERE mark>50")
items = cursor.fetchall()
for item in items:
    print(item)

print("\n")

# TASK - Find student using subject
print("STUDENT MARKS IN CE \n")
s=["ce"]
cursor.execute("SELECT * FROM student_marks WHERE subject = (?)",s)

items = cursor.fetchall()
for item in items:
    print(item)
conn.commit()
conn.close()