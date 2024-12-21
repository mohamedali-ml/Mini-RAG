from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def hello_world():
    return {"message": "Welcome to you!"}