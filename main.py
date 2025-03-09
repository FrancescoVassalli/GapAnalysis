import asyncio
import logging
import os

import uvicorn
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import Database
import ana

logger = logging.getLogger("Main")

load_dotenv(find_dotenv())


app = FastAPI()
app.include_router(ana.router)


@app.get("/")
async def read_main():
    return {"msg": "LLM-KG-API"}


allow_origins = [
    "https://localhost:5173",
    "http://localhost:5173",
    "http://localhost:5173/",
    "https://localhost:5173/",
    "localhost:5173",
    "localhost:5173/",
    "https://localhost:5173",
    "https://172.18.0.2:5173",
    "https://172.18.0.1:5173",
    "http://172.18.0.1:5173",
    "172.18.0.1:5173",
    "https://172.18.0.1",
    "https://172.18.0.1:*",
    "https://172.18.0.1:55554",
    "https://172.18.0.1:55558",
    "https://172.18.0.4:5173",
    "https://172.18.0.3:5173",
    "http://127.0.0.1:5173",
    "https://127.0.0.1:5173",
    "127.0.0.1:5173",
    "http://0.0.0.0:5173",
    "0.0.0.0:5173",
    "http://0.0.0.0:5173",
    "http://127.0.0.1:3000",
    "localhost:3000",
    "http://localhost:3000",
    "https://0.0.0.0:5173",
]


if os.getenv("ENV") == "development":
    logger.warning("Establishing CORS for development ")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_origin_regex="^https:\/\/(.*\.)?tryrecess\.vercel\.app$",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

db = Database()
app.state.db = db

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
