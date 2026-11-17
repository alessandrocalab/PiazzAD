import uvicorn
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from app.api.router import api_router

load_dotenv()


app=FastAPI(title="PiazzAD API", version="0.1.0")
app.include_router(api_router)


if __name__=="__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("FASTAPI_HOST", "127.0.0.1"),
        port=int(os.getenv("FASTAPI_PORT", "8080")),
        reload=os.getenv("FASTAPI_RELOAD", "false").lower()=="true"
    )