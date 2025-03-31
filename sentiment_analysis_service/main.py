from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# API key and endpoint
API_KEY = os.getenv("OPENAI_API_KEY")
API_URL = os.getenv("OPENAI_API_URL") 

if not API_KEY:
    raise ValueError("API key not found. Please set it in the .env file.")

# Request model
class SentimentRequest(BaseModel):
    text: str

@app.post("/analyze-sentiment/")
async def analyze_sentiment(request: SentimentRequest):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "messages": [
            {"role": "system", "content": "You are a sentiment analysis assistant."},
            {"role": "user", "content": f"Analyze the sentiment of the following text and reply only with one word: {request.text}"}
        ],
        "max_tokens": 60,
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    result = response.json()
    sentiment = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    return {"sentiment": sentiment}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)