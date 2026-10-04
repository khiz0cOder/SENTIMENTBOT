# SentimentBot

A real time sentiment analysis API built with FastAPI and HuggingFace Transformers.

## What it does

Send any text — a review, a tweet, a comment — and get back a sentiment label (POSITIVE/NEGATIVE) with a confidence score.

## API

**Endpoint:** `POST /analyze`

**Request:**
```json
{"text": "This product is amazing!"}
```

**Response:**
```json
{"text": "This product is amazing!", "sentiment": "POSITIVE", "confidence": 0.9998}
```

## Stack

- **FastAPI** — API framework
- **HuggingFace Inference API** — DistilBERT model for sentiment classification
- **Render** — deployment

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Live demo

API: https://sentimentbot.onrender.com  
Frontend: open `index.html` in your browser

---

Part of my AI Engineering portfolio. building projects that use the same stack production teams use.