from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hello FastAPI!"

@app.get("/url")

async def url():
    return {"class_url":"https://mouredev.com/python"}

