"""
Main application entry point.
Written with extensive comments for learning purposes.
"""
from fastapi import FastAPI
from app.routes.text_routes import router as text_router

app = FastAPI(title="Multimodal Hate Speech Detector")

app.include_router(text_router)

@app.get("/")
def home():
    return {"message": "Application is running"}
