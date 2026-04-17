#DAY 106
import sqlite3

#connect to database 
conn = sqlite3.connect("notes.db")
#create cursor
cursor= conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes(
    id INTEGER PRIMARY KEY,
    text TEXT
)

""")

cursor.execute("INSERT INTO notes (text) VALUES (?)",("MY first note",))
conn.commit()

cursor.execute("SELECT*FROM notes")
data= cursor.fetchall()

print(data)
conn.close()
