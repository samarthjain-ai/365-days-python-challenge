import bcrypt

def hash_password(password):
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return hashed.decode()


password = "bob12345"

hashed_password = hash_password(password)

print("Original:", password)
print("Hashed:", hashed_password)