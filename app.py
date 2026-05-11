from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle

# Initialize app
app = FastAPI()

# Templates (IMPORTANT: keep this exactly like this)
templates = Jinja2Templates(directory="templates")

# Load model + vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


# Home route (loads website)
@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


# Prediction route
@app.post("/predict")
async def predict(file: UploadFile = File(None), code: str = Form(None)):

    # If file uploaded → read it
    if file:
        content = await file.read()
        code = content.decode("utf-8", errors="ignore")

    # If nothing provided → prevent crash
    if not code:
        return {"error": "No code provided"}

    # Transform + predict
    vec = vectorizer.transform([code])
    pred = model.predict(vec)[0]

    # Confidence (if available)
    confidence = None
    if hasattr(model, "predict_proba"):
        confidence = model.predict_proba(vec).max()

    return {
        "language": pred,
        "confidence": float(confidence) if confidence else None
    }