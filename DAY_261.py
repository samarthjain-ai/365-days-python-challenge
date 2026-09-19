import bcrypt

def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

def verify_password(password, hashed_password):
    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode()
    )

users = [
    {
        "username": "samarth",
        "email": "test@example.com",
        "password": hash_password("bob12345")
    }
]

def authenticate_user(username, password):

    for user in users:
        if user["username"] == username:

            if verify_password(password, user["password"]):
                return {"username": user["username"]}

            else:
                return "Invalid Password"

    return "User NOT Found"

print(authenticate_user("samarth", "bob12345"))
print(authenticate_user("samarth", "wrongpass"))
print(authenticate_user("unknown", "bob12345"))