from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

def get_frontend_path():  
    cur_p = os.path.join(os.curdir, "frontend", "build")
    return cur_p

app = FastAPI()

@app.get("/api/test")
async def index():
    return { "message": "Hello there, help me I am stuck in an endless time warp!" }

app.mount("/", StaticFiles(directory=get_frontend_path(), html=True), name="frontend")

