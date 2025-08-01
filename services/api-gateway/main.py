from fastapi import FastAPI
from router import router

app = FastAPI(title="API Gateway")
app.include_router(router)
