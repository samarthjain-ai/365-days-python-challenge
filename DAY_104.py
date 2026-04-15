# DAY 104 - Notes API
from fastapi import FastAPI
app = FastAPI()

# Data storage
notes = []
note_id = 1


@app.get("/")
def home():
    return {"message": "Notes API running 🚀"}


@app.post("/add")
def add_note(note: str):
    global note_id

    new_note = {
        "id": note_id,
        "text": note
    }

    notes.append(new_note)
    note_id += 1

    return {"message": "Note added", "note": new_note}


# Get all notes
@app.get("/notes")
def get_notes():
    return {"notes": notes}


# Get note by ID
@app.get("/note/{id}")
def get_note(id: int):
    for note in notes:
        if note["id"] == id:
            return note
    return {"error": "Note not found"}


# Delete note
@app.delete("/delete/{id}")
def delete_note(id: int):
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            return {"message": "Note deleted"}
    return {"error": "Note not found"}