import os
import json
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv('.env.example')

app = FastAPI(title="LLM Core Service")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "qwen/qwen3-coder:free"

class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 256
    temperature: float = 0.7

@app.post("/generate")
def generate(req: GenerateRequest):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": os.getenv("HTTP_REFERER", "http://localhost"),
        "X-Title": os.getenv("X_TITLE", "Local LLM Service"),         
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": req.prompt}],
        "max_tokens": req.max_tokens,
        "temperature": req.temperature,
    }
    try:
        response = requests.post(
            url=OPENROUTER_API_URL,
            headers=headers,
            data=json.dumps(payload)
        )
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        return {"response": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/model_info")
def model_info():
    return {"model": MODEL_NAME, "provider": "openrouter.ai"}
