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



users=[]

def authenticate_user(username, password):


    for user in users:
        if user["username"]==username:

                if verify_password(password,user["password"]):
                    return "Access Given"

                else:
                    return "Incorrect password"
                
    else:
        return "User not found"

print(authenticate_user("ghj","fgh"))