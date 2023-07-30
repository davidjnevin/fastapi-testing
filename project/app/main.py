from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/ping")
async def read_main():
    return {"msg": "pong"}
