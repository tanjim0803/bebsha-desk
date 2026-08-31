from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is BebshaDesk App"}
