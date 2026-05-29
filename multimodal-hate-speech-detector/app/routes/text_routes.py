from fastapi import APIRouter
from pydantic import BaseModel
from app.services.text_analysis import analyze_text

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/analyze/text")
def analyze(data: TextRequest):
    return analyze_text(data.text)
