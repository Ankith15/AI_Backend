from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.schemas.token import Token
from app.utils.hash import hash_password, verify_password
from app.utils.jwt import create_access_token

router = APIRouter(tags=["Auth"])
templates = Jinja2Templates(directory="app/templates")

# API-based register (still useful for testing in Swagger or Postman)
@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
        role="Viewer"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#  HTML form: render register page
@router.get("/register-form", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

#  HTML form: handle user registration
@router.post("/register-form", response_class=HTMLResponse)
def register_user_form(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Email already registered"
        })

    new_user = User(
        username=username,
        email=email,
        hashed_password=hash_password(password),
        role="Viewer"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return RedirectResponse(url="/", status_code=302)

#  Combined login route (form + JWT + redirect to dashboard)
@router.post("/login", response_class=HTMLResponse)
def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Invalid credentials"
        })

    access_token = create_access_token(data={"sub": user.email})
    response = RedirectResponse(url="/dashboard", status_code=302)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return response
