import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.api.deps import get_db
from app.models.models import Base

# Setup a temporary test database (SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
Base.metadata.drop_all(bind=engine)  
Base.metadata.create_all(bind=engine)
client = TestClient(app)

@pytest.fixture
def auth_headers():
    # Use unique email for each test run to avoid "User already exists" errors
    import uuid
    email = f"user_{uuid.uuid4()}@example.com"
    password = "testpassword"
    client.post("/auth/register", json={"email": email, "password": password})
    response = client.post("/auth/login", data={"username": email, "password": password})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_create_and_update_note_versioning(auth_headers):
    res = client.post("/notes/", headers=auth_headers, json={"title": "V1", "content": "Original"})
    assert res.status_code == 200
    note_id = res.json()["id"]

    update_res = client.put(f"/notes/{note_id}", headers=auth_headers, json={"title": "V1", "content": "Updated"})
    assert update_res.status_code == 200

    version_res = client.get(f"/notes/{note_id}/versions", headers=auth_headers)
    assert version_res.status_code == 200
    assert len(version_res.json()) >= 1
    assert version_res.json()[0]["content_snapshot"] == "Original"

def test_search_functionality(auth_headers):
    # Create two notes
    client.post("/notes/", headers=auth_headers, json={"title": "Grocery List", "content": "Buy milk"})
    client.post("/notes/", headers=auth_headers, json={"title": "Workout Routine", "content": "Leg day"})

    # Search for "Grocery"
    res = client.get("/notes/?q=Grocery", headers=auth_headers)
    assert res.status_code == 200
    assert len(res.json()) == 1
    assert res.json()[0]["title"] == "Grocery List"

    # Search for "milk" (case-insensitive content search)
    res_content = client.get("/notes/?q=milk", headers=auth_headers)
    assert len(res_content.json()) == 1
    assert "milk" in res_content.json()[0]["content"]

def test_restore_version(auth_headers):
    # 1. Create and update a note
    res = client.post("/notes/", headers=auth_headers, json={"title": "Old", "content": "Snapshot 1"})
    note_id = res.json()["id"]
    client.put(f"/notes/{note_id}", headers=auth_headers, json={"title": "New", "content": "Snapshot 2"})

    # 2. Restore to version 1
    restore_res = client.post(f"/notes/{note_id}/restore/1", headers=auth_headers)
    assert restore_res.status_code == 200
    assert restore_res.json()["content"] == "Snapshot 1"

def test_unauthorized_access():
    res = client.get("/notes/")
    assert res.status_code == 401