from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.resource import Resource
from app.utils.jwt import decode_access_token
from jose import JWTError

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/resource/upload")
def upload_form(request: Request):
    return templates.TemplateResponse("upload_resource.html", {"request": request})

@router.post("/resource/upload")
def upload_resource(
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    token = request.cookies.get("access_token")
    try:
        user_data = decode_access_token(token.split(" ")[1])
        user_email = user_data["sub"]

        new_res = Resource(title=title, content=content, created_by=user_email)
        db.add(new_res)
        db.commit()
        return RedirectResponse("/resource/view", status_code=302)

    except JWTError:
        return RedirectResponse("/", status_code=302)

@router.get("/resource/view")
def view_resources(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    try:
        user_data = decode_access_token(token.split(" ")[1])
        user_email = user_data["sub"]

        resources = db.query(Resource).filter(Resource.created_by == user_email).all()
        return templates.TemplateResponse("view_resources.html", {
            "request": request,
            "resources": resources,
            "user": user_email
        })

    except JWTError:
        return RedirectResponse("/", status_code=302)

# ✅ Guest view (no login required)
@router.get("/guest/resource/{resource_id}")
def guest_view_resource(resource_id: int, request: Request, db: Session = Depends(get_db)):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()

    if not resource:
        return RedirectResponse("/", status_code=404)

    return templates.TemplateResponse("guest_view.html", {
        "request": request,
        "title": resource.title,
        "content": resource.content,
        "owner": resource.created_by
    })

