from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DocVerify Lite running. Try /health"}

@app.get("/health")
def health():
    return {"status": "ok"}
