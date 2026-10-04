from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

sentiment_model = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "SentimentBot is running"}

@app.post("/analyze")
def analyze(input: TextInput):
    result = sentiment_model(input.text)[0]
    return {
        "text": input.text,
        "sentiment": result["label"],
        "confidence": round(result["score"], 4)
    }