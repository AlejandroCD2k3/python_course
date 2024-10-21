from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Path decorator for Root path | Local URL: http://127.0.0.1:8000/
async def root():
    return "Hello FastAPI!"

@app.get("/url") # Path decorator for Url path | Local URL: http:/127.0.0.1:8000/url

async def url():
    return {"class_url":"https://mouredev.com/python"}


# Starting uvicorn server: python -m uvicorn main:app --reload
# Stopping server: CTRL + C (^C)

# Swagger documentation: http://127-0.0.1:8000/docs
# Redocly documentation: http://127-0.0.1:8000/redoc
