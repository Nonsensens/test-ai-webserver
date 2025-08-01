import httpx

LLM_URL = "http://llm_server:8001"

async def ask_llm(data: dict):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{LLM_URL}/generate", json=data, timeout=100)
        resp.raise_for_status()
        return resp.json()["response"]

async def get_llm_info():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{LLM_URL}/model_info")
        resp.raise_for_status()
        return resp.json()
