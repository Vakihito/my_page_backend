from fastapi import FastAPI
from src.main.factory import setup_router_factories

app = FastAPI()

setup_router_factories(app)


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/lifes_meaning")
async def root():
    return {"meaning": 42}
