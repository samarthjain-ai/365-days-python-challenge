import sqlite3
def create():
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
               first_name text,
               last_name text,
               email text
        )
    """) 
    conn.commit()
    conn.close()
def show_all():

    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()

    cursor.execute("SELECT rowid, * FROM customers")
    items = cursor.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()

def add_one(First,last,email):

    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO customers VALUES (?,?,?)",(First,last,email))

    conn.commit()
    conn.close()

def delete_one(id):
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()   

    cursor.execute("DELETE FROM customers WHERE rowid =(?)",(id,) )

    conn.commit()
    conn.close()

def add_many(list):
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO customers VALUES (?,?,?)",(list))

    conn.commit()
    conn.close()

def define_lookup(email):
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers WHERE email = (?)",(email,))

    items = cursor.fetchall()

    for item in items:
        print(item)
    conn.commit()
    conn.close()

create()
add_one('me','self','me12@gmail.com')
data=[
    ('a','z','az2@gmail.com'),
    ('b','y','by3@gmail.com')
]
add_many(data)
define_lookup(2)
delete_one(2)
show_all()