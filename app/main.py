from fastapi import FastAPI
from app.api import auth, notes

app = FastAPI(title="Notes API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(notes.router, prefix="/notes", tags=["notes"])

@app.get("/")
def health_check():
    return {"status": "healthy"}