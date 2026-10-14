
import sqlite3

def get_connection():
    connection = sqlite3.connect("github_clon.db")
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

    result = insert_user(
        "samarth_test_2",
        "samarth_t2@example.com",
        "dummy_hash_testing"
    )

    print(result)


