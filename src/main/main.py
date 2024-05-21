from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/lifes_meaning")
async def root():
    return {"meaning": 42}
