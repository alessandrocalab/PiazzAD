import os

import uvicorn
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")
host = os.getenv("FASTAPI_HOST", "127.0.0.1")
port = int(os.getenv("FASTAPI_PORT", "8000"))
reload = os.getenv("FASTAPI_RELOAD", "false").lower() == "true"

uvicorn.run("app.main:app", host=host, port=port, reload=reload)
