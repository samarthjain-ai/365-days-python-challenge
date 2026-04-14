#DAY 103
#---My First APL ---

# IN TERMINAL - pip install fastapi uvicorn

from fastapi import FastAPI
import random
app = FastAPI()

number =random.randint(1,100)
@app.get("/")
def home():
    return{"message":"Guessing Game API"}

@app.get("/guess")
def guess_number(user_input:int):
    if user_input>number:
        return{"Result": "Too High"}
    elif user_input<number:
        return{"Result":"Too Low"}
    else:
        return {"Result":"Correct"}
    