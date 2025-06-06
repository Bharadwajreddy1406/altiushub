

# Full-Stack ToDo List & User CRUD App

This repository is organized into two rounds:

* **Round 1:** Includes two initial questions/solutions.
* **Round 2:** Contains a full-stack implementation of a **ToDo List frontend** and a **Django backend** for user CRUD operations with JWT authentication.

---

## 📁 Project Structure

```
.
├── round1/
│   ├── q1/                # Solution to the first question
│   └── q2/                # Solution to the second question
├── round2/
│   ├── frontend/          # React-based ToDo List App
│   └── backend-crud/      # Django User CRUD App with JWT Auth
└── README.md
```

---

## 🚀 Round 2: Project Details

### 1. 📝 Frontend: ToDo List App

**Tech Stack:** React, Axios, CSS

#### Features:

* Add, edit, and delete tasks
* Mark tasks as complete
* Responsive UI

#### Setup Instructions:

```bash
cd round2/frontend
npm install
npm start
```

---

### 2. 🔐 Backend: Django User CRUD with JWT Authentication

**Tech Stack:** Django, Django REST Framework, SimpleJWT

#### Features:

* Register, login, logout users
* JWT-based authentication
* CRUD operations on user model

#### Setup Instructions:

```bash
cd round2/backend-crud
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### API Endpoints:

* `POST /api/create-user/` – Create a new user
* `GET /api/get-all-users/` – Retrieve all users
* `PUT /api/update-user/<user_id>/` – Update user by ID
* `PATCH /api/update-user/<user_id>/` – Partially update user by ID
* `DELETE /api/delete-user/<user_id>/` – Delete user by ID

---

**Note:** Currently, these endpoints do **not** require authentication. To secure them, consider using:
```python
@authentication_classes([CookieJWTAuthentication])
@permission_classes([IsAuthenticated])


