# 📝 Notes API with Version History



A FastAPI-based backend for managing personal notes with JWT authentication.

## 🚀 Deployment & API Testing
- **Live API URL:** `https://notes-api-backend-dchf.onrender.com`
- **Postman Collection:** [Access Collection Here](https://abhimanue-5326258.postman.co/workspace/Abhimanue's-Workspace~dad1ed39-b494-474d-8fe1-6873c26592a5/collection/46314708-58d7a0b3-8414-435d-af72-1c453fb233ba?action=share&source=copy-link&creator=46314708)

## 🛠️ How to Test
1. **Import the Collection:** Use the link above to view/import the requests.
2. **Environment Setup:** Ensure the `base_url` variable is set to `notes-api-backend-dchf.onrender.com`.
3. **Authentication:** - Run the **Register** and **Login** requests first.
   - The login request has a test script that automatically saves the `access_token` to your variables.
   - if sometimes the token will not populate to other api request if that happens try to refresh or change the token manually
4. **CRUD Flow:** - Once logged in, you can Create, Get, Update, and Delete notes. 
   - All protected routes automatically use the Bearer token.

![Python](https://img.shields.io/badge/Python-3.13-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue) ![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)

A production-ready backend API for managing personal notes. This project goes beyond basic CRUD by implementing **Automatic Version Control**, allowing users to track changes, search their notes, and restore previous versions of their content.

---

## 🚀 Key Features

### ✅ Core Functionality
* **Secure Authentication:** User registration and login using **JWT (JSON Web Tokens)** and **Bcrypt** hashing.
* **Note Management:** Full Create, Read, Update, Delete (CRUD) support.
* **Data Integrity:** Users can only access and modify their own notes.

### ✨ Advanced Features (Bonus)
* **🔄 Automatic Versioning:** Every `UPDATE` action automatically saves a snapshot of the note's content to a history table.
* **⏮️ Restore Capability:** Users can revert a note to any previous version using the `/restore` endpoint.
* **🔍 Smart Search:** Server-side filtering allows users to search notes by title or content (e.g., `GET /notes/?q=shopping`).

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Framework** | FastAPI | High-performance async web framework. |
| **Database** | PostgreSQL | Relational database for robust data storage. |
| **ORM** | SQLAlchemy | Python SQL toolkit and Object Relational Mapper. |
| **Migrations** | Alembic | Database schema version control. |
| **Testing** | Pytest | Comprehensive test suite for Unit and Integration testing. |

---

## 🔧 Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPO_URL_HERE>
cd notes-api-assessment 
```

### 2. Create Virtual Environment
Isolate the project dependencies by creating a virtual environment.

**For Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. 📥 Install Dependencies
Install all required libraries, including FastAPI, SQLAlchemy, and the testing suite.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. 🔑 Environment Variables

Create a `.env` file in the root directory. This file stores your sensitive credentials and is ignored by Git for security.

```env
# Database Configuration
DATABASE_URL=postgresql://postgres:password@localhost:5432/notes_db

# Security Settings
SECRET_KEY=your_super_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run Database Migrations
Initialize the database schema using Alembic:
```alembic upgrade head```

### 6. Start the Server
```uvicorn app.main:app --reload```

### 7. 🧪 Testing
```pytest```




## 📮 Postman Documentation (Mandatory)

This project includes a comprehensive Postman Collection to test and verify all API endpoints.

### 🛠️ Setup & Import
1. **File Location:** The collection file is located at `/docs/Notes_API.postman_collection.json`.
2. **Import:** Open Postman, click **Import**, and select the file from this repository.
3. **Environment:** The collection uses a `{{base_url}}` variable. By default, it is set to `http://127.0.0.1:8000`.

### 🔐 Authentication Flow
- The collection is configured with a **Collection-level Bearer Token**.
- **Automatic Login:** When you run the `Admin Login` request, a post-response script automatically saves the `access_token` to the collection variables.
- All protected routes (Notes, Search, Versioning) inherit this token automatically.

### ✅ Features Included
- **Saved Examples:** Every request includes an "Example" showing the expected input and output.
- **Validation Scripts:** Every request includes automated tests to verify:
  - Status codes (200 OK, 201 Created, 204 No Content).
  - Data integrity (checking for arrays and object structures).
- **Descriptive Bodies:** All POST and PUT requests come pre-loaded with sample JSON data.

### 📧 Cloud Access
In accordance with the requirements, access to the live Postman collection has been shared with:
- `jmrpatel257@gmail.com`
- `workemail.rajat@gmail.com`


