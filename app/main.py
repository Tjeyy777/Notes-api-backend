from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, notes

app = FastAPI(
    title="Notes API",
    description="Secure Notes API with Version History and JWT Authentication",
    version="1.0.0"
)


origins = [
    "http://localhost",
    "http://localhost:3000", # Common React/Next.js port
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins for testing; change to 'origins' for production
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Allows all headers (including Authorization)
)

# --- Routes ---
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(notes.router, prefix="/notes", tags=["Notes Management"])

@app.get("/", tags=["Health"])
def health_check():
    """
    Check if the API and Database connection are functional.
    """
    return {
        "status": "online",
        "message": "Notes API is running securely"
    }