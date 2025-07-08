from fastapi import APIRouter, Request, Depends, Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.db.database import get_db
from app.models.org import Organization
from app.models.dept import Department
from app.utils.jwt import decode_access_token
from jose import JWTError

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# GET: Org Form
@router.get("/org/create-form")
def create_org_form(request: Request):
    return templates.TemplateResponse("create_org.html", {"request": request})

# POST: Create Org with duplicate check + real user
@router.post("/org/create-form")
def create_org(request: Request, name: str = Form(...), db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        return RedirectResponse("/", status_code=302)

    try:
        user_data = decode_access_token(token.split(" ")[1])
        user_email = user_data["sub"]

        existing_org = db.query(Organization).filter(Organization.name == name).first()
        if existing_org:
            return templates.TemplateResponse("create_org.html", {
                "request": request,
                "error": "❗ Organization already exists."
            })

        org = Organization(name=name, created_by=user_email)
        db.add(org)
        db.commit()
        return RedirectResponse("/dashboard", status_code=302)

    except JWTError:
        return RedirectResponse("/", status_code=302)

# GET: Dept Form
@router.get("/dept/create-form")
def create_dept_form(request: Request, db: Session = Depends(get_db)):
    orgs = db.query(Organization).all()
    return templates.TemplateResponse("create_dept.html", {
        "request": request,
        "orgs": orgs
    })

# POST: Create Dept
@router.post("/dept/create-form")
def create_dept(request: Request, name: str = Form(...), org_id: int = Form(...), db: Session = Depends(get_db)):
    dept = Department(name=name, org_id=org_id)
    db.add(dept)
    db.commit()
    return RedirectResponse("/dashboard", status_code=302)
