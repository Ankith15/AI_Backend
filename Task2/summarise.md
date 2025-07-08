```markdown
# 🔹 RBAC System - Summary

This is a minimal Role-Based Access Control (RBAC) system built with FastAPI.
---

## ✅ Features Implemented

- User registration and JWT-based login
- Create organizations and departments
- Assign roles (Admin, Editor, Viewer)
- Upload and view text-based resources
- Generate guest-accessible resource links
- Web UI using Jinja2 templates
- Auth-protected routes with role-based logic

---

## 🏗️ Tech Stack

- **Framework**: FastAPI
- **Database**: MySQL (via SQLAlchemy)
- **Auth**: OAuth2 + JWT (`python-jose`)
- **Templates**: Jinja2 (HTML)
- **Password Hashing**: passlib
- **Session Management**: Cookies

---

## 📂 Project Structure

```

app/
├── db/                # DB engine
├── models/            # SQLAlchemy models
├── routes/            # API and form routes
├── templates/         # HTML templates
├── utils/             # Hashing + JWT helpers
└── main.py            # FastAPI entry point

```

---

## 📮 Key Endpoints

| Route                          | Purpose                      |
|--------------------------------|------------------------------|
| `/register`, `/login`         | Auth with JWT                |
| `/org/create-form`            | Create organization          |
| `/dept/create-form`           | Create department            |
| `/assign-role`                | Assign role to user          |
| `/resource/upload`            | Upload resource              |
| `/resource/view`              | View uploaded resources      |
| `/guest/resource/{id}`        | Public link for guest access |

---

