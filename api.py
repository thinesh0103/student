from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from JSON file
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

# Convert list to a dictionary for quick lookup
student_marks = {student["name"]: student["marks"] for student in data}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    marks = [student_marks.get(n, None) for n in name]
    return {"marks": marks}

