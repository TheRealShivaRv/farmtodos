from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:8000'
]


def get_frontend_path():
    cur_p = os.path.join(os.curdir, "frontend", "build")
    return cur_p


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=ALLOWED_ORIGINS,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/api/test")
async def index():
    return {"message": "Hello there, help me I am stuck in an endless time warp!"}

app.mount("/", StaticFiles(directory=get_frontend_path(),
          html=True), name="frontend")
