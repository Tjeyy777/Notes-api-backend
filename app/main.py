from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, notes

app = FastAPI(
    title="Notes API",
    description="Secure Notes API with Version History and JWT Authentication",
    version="1.0.0"
)

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# --- Routes ---
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(notes.router, prefix="/notes", tags=["Notes Management"])

@app.get("/", tags=["Health"])
def health_check():
    return {
        "status": "online",
        "message": "Notes API is running securely"
    }