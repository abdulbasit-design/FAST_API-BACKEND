# 🚀 FastAPI Backend — JWT Authentication & Role-Based Todo API

A backend REST API built with **FastAPI**, **MongoDB**, **Pydantic**, **JWT authentication**, and **role-based authorization**.

This project was built as a learning project to understand how a real-world FastAPI backend works, including CRUD operations, authentication, authorization, password hashing, JWT tokens, user roles, and resource ownership.

---

## 📌 Project Overview

This backend provides a Todo management API where:

- Users can register and login.
- Passwords are securely hashed before being stored.
- Login generates a JWT access token.
- Protected routes require a valid JWT.
- Every user can manage their own Todos.
- Users cannot access or modify another user's Todos.
- Admins can manage all Todos.
- Admin-only routes are protected using role-based authorization.
- MongoDB is used as the database.
- APIs can be tested using Postman or Swagger UI.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend web framework |
| Uvicorn | ASGI server |
| MongoDB | Database |
| PyMongo | MongoDB connection/operations |
| Pydantic | Request validation |
| JWT | Authentication |
| HTTPBearer | Bearer token authentication |
| Password Hashing | Secure password storage |
| Postman | API testing |
| Swagger UI | API documentation/testing |

---

# 📂 Project Structure

```text
FAST_API-BACKEND/
│
├── app/
│   │
│   ├── database/
│   │   └── connection.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   └── todos.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   └── todo.py
│   │
│   ├── utils/
│   │   ├── auth.py
│   │   ├── jwt.py
│   │   └── password.py
│   │
│   └── main.py
│
├── create_admin.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md