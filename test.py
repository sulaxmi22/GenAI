from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def add(a, b):
    return {"result": a + b}

print(add(2, 3))