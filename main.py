from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

HF_API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
HF_TOKEN = os.environ.get("HF_TOKEN", "")

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "SentimentBot is running"}

@app.post("/analyze")
def analyze(input: TextInput):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}
    response = httpx.post(HF_API_URL, json={"inputs": input.text}, headers=headers)
    result = response.json()[0][0]
    return {
        "text": input.text,
        "sentiment": result["label"],
        "confidence": round(result["score"], 4)
    }