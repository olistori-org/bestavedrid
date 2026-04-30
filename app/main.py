from fastapi import FastAPI

app = FastAPI()

count = 0

@app.get("/hello")
def hello():
    global count
    count += 1
    return {"message": f"Hello World {count}"}

@app.get("/health")
def health():
    return {"status": "ok"}