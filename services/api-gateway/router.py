from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from client import ask_llm, get_llm_info

router = APIRouter()

class AskRequest(BaseModel):
    prompt: str
    max_tokens: int = 256
    temperature: float = 0.7

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/ask")
async def ask(req: AskRequest):
    try:
        result = await ask_llm(req.model_dump())
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/info")
async def info():
    return await get_llm_info()
