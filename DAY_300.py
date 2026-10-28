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


if __name__ == "__main__":
    create_users_table()

    print("Testing database connection...")
    connection = get_connection()
    print("Connection successful!")
    connection.close()

    print("\nTesting user insertion...")
    try:
        result = insert_user(
            "samarth_test_300",
            "samarth300@example.com",
            "dummy_password_123"
        )
        print(result)
    except sqlite3.IntegrityError:
        print("User already exists: duplicate username or email.")

    print("\nTesting completed.")
