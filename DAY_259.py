import bcrypt


def hash_password(password):
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )
    return hashed.decode()


def verify_password(password, hashed_password):
    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode()
    )


password = "bob12345"

hashed = hash_password(password)

print("Stored hash:", hashed)

print(verify_password("bob12345", hashed))
print(verify_password("wrongpass", hashed))