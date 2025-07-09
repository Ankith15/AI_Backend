from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load model and scaler
with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("heart_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
def form_post(
    request: Request,
    Age: int = Form(..., ge=0),
    Sex_F: int = Form(..., ge=0, le=1),
    ChestPainType_ATA: int = Form(..., ge=0, le=1),
    ChestPainType_NAP: int = Form(..., ge=0, le=1),
    ChestPainType_TA: int = Form(..., ge=0, le=1),
    RestingBP: float = Form(..., ge=0),
    Cholesterol: float = Form(..., ge=0),
    FastingBS: int = Form(..., ge=0, le=1),
    RestingECG_Normal: int = Form(..., ge=0, le=1),
    RestingECG_ST: int = Form(..., ge=0, le=1),
    MaxHR: float = Form(..., ge=0),
    ExerciseAngina_Y: int = Form(..., ge=0, le=1),
    Oldpeak: float = Form(..., ge=0),
    ST_Slope_Flat: int = Form(..., ge=0, le=1),
    ST_Slope_Up: int = Form(..., ge=0, le=1)
):
    try:
        data = np.array([[Age, Sex_F, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA,
                          RestingBP, Cholesterol, FastingBS, RestingECG_Normal, RestingECG_ST,
                          MaxHR, ExerciseAngina_Y, Oldpeak, ST_Slope_Flat, ST_Slope_Up]])
        scaled = scaler.transform(data)
        prediction = int(model.predict(scaled)[0])
    except Exception as e:
        prediction = f"Error: {str(e)}"

    return templates.TemplateResponse("form.html", {
        "request": request,
        "prediction": prediction
    })
