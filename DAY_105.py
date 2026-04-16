#DAY 105
from fastapi import FastAPI

app= FastAPI()

notes =[]  #Stroage
note_id =1 # unique id


@app.get("/")
def home():
    return {"Message":"Notes API running"}
@app.post("/add")
def add_note(note:str):
    global note_id
    new_note= {
        "id":note_id,
        "text":note
    }
    notes.append(new_note)
    note_id+=1
    return {"message":"Note added","note":new_note}

@app.get("/notes")
def get_Notes():
    return {"notes":notes}

@app.get("/note/{id}")
def get_note_id(id:int):
    for note in notes:
        if note["id"] ==id:
            return {"notes":note}
    return {"Error":"Notes not found"}

@app.delete("/delete/{id}")
def delete_note(id:int):
    for note in notes:
        if note["id"]==id:
            notes.remove(note)
            return {"messsage":"Notes delete "}
    return {"Id not found"}

@app.put("/update/{id}")
def note_update(id:int,new_text:str):
    for note in notes:
        if note["id"]==id:
            note["text"]=new_text
            return {"message":"updated","note":note}
    return {"Invalid input"}




