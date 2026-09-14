from fastapi import FastAPI
from pydantic import BaseModel , EmailStr , Field

class UserRegister(BaseModel):
    username : str
    email : EmailStr
    password : str = Field(min_length= 8,max_length= 16, description= "User password must be 8-16 characters long")

app= FastAPI()
@app.post("/UserRegister")
def userregister(user:UserRegister):

    result = register_user(user.username, user.email, user.password)
    return result


users=[]

def register_user(username, email, password):
    for existing_user  in users:
        if existing_user ["username"] == username:
            return {"message":"username Exist"}
        elif existing_user ["email"] ==email:
            return {"message":"email exist"}
    else:

        users.append(
            {
                "username":username,
                "email":email,
                "password":password
            }
        )

        return {
        "message" : "Account Created",
        "data" : {
        "username":username,
        "Email" : email
            }
        }



