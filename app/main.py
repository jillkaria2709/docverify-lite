from fastapi import FastAPI
from datasets import load_dataset

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DocVerify Lite running. Try /health"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/dataset_info")
def dataset_info():
    ds = load_dataset("rvl_cdip", split="train[:1]")
    return {
        "len": len(ds),
        "columns": ds.column_names,
        "label0": int(ds[0]["label"]),
    }
