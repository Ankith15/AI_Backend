from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from jose import JWTError
from sqlalchemy.orm import Session

# Models
from app.models import user, org, dept
from app.models.org import Organization
from app.models.dept import Department
from app.models import resource  



# Database
from app.db.database import engine, get_db

# Routes
from app.routes import auth
from app.routes import org_dept
from app.routes import roles
from app.routes import resources


# Utils
from app.utils.jwt import decode_access_token

# FastAPI app init
app = FastAPI()

# Auto-create DB tables
user.Base.metadata.create_all(bind=engine)
org.Base.metadata.create_all(bind=engine)
dept.Base.metadata.create_all(bind=engine)
resource.Base.metadata.create_all(bind=engine)


# Routers
app.include_router(auth.router)
app.include_router(org_dept.router)
app.include_router(roles.router)
app.include_router(resources.router)


# Jinja2 templates directory
templates = Jinja2Templates(directory="app/templates")

# ✅ Homepage → Login Page
@app.get("/", tags=["Frontend"])
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# ✅ Protected Dashboard
@app.get("/dashboard", tags=["Frontend"])
def dashboard(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        return RedirectResponse("/", status_code=302)

    try:
        # Decode token
        user_data = decode_access_token(token.split(" ")[1])
        user_email = user_data["sub"]

        # Check if user has created org
        org = db.query(Organization).filter(Organization.created_by == user_email).first()
        dept = db.query(Department).first()  # (You can filter by org_id if needed)

        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "user": user_email,
            "org_exists": bool(org),
            "dept_exists": bool(dept)
        })

    except JWTError:
        return RedirectResponse("/", status_code=302)
