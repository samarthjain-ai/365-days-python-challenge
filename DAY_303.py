import sqlite3

def get_connection():
    connection = sqlite3.connect("githubclone.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_users_table():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

def insert_user(username, email, password):
    connection = get_connection()

    connection.execute("""
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?)
    """, (username, email, password))

    connection.commit()
    connection.close()

    return "User inserted successfully!"


def get_user_by_username(username):
    connection = get_connection()

    result = connection.execute("""
        SELECT * FROM users
        WHERE username = ?
    """, (username,))

    user = result.fetchone()

    connection.close()

    return user


def get_user_by_email(email):
    connection = get_connection()

    result = connection.execute("""
        SELECT * FROM users
        WHERE email = ?
    """, (email,))

    user = result.fetchone()

    connection.close()

    return user



def user_exists(username, email):
    connection = get_connection()

    query = """
        SELECT * FROM users
        WHERE username = ? OR email = ?
    """

    result = connection.execute(query, (username, email))
    record = result.fetchone()

    connection.close()

    return record is not None




def get_user_by_id(user_id):
    connection = get_connection()

    query = """
        SELECT * FROM users
        WHERE id = ?
    """

    result = connection.execute(query, (user_id,))
    record = result.fetchone()

    connection.close()

    return record




print("\nTesting user existence...")

print(user_exists(
    "samarth_test_300",
    "samarth300@example.com"
))

print("\nTesting user ID lookup...")

user = get_user_by_id(1)

if user:
    print("User found:", dict(user))
else:
    print("User not found.")


