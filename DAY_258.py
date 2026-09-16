from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
import bcrypt


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=16,
        description="User password must be 8-16 characters long"
    )


app = FastAPI()

users = []

def hash_password(password):
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return hashed.decode()


def register_user(username, email, password):

    for existing_user in users:

        if existing_user["username"] == username:
            return {"message": "Username already exists"}

        elif existing_user["email"] == email:
            return {"message": "Email already exists"}

    hashed_password = hash_password(password)

    users.append({
        "username": username,
        "email": email,
        "password": hashed_password
    })

    return {
        "message": "Account Created",
        "data": {
            "username": username,
            "email": email
        }
    }


@app.post("/UserRegister")
def user_register(user: UserRegister):

    result = register_user(
        user.username,
        user.email,
        user.password
    )

    return result