from pathlib import Path
from fastapi import FastAPI, UploadFile, File

from app.services.extractor import extract_invoice

app = FastAPI()

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


@app.get("/")
def root():
    return {
        "message": "Invoice extractor API running"
    }

@app.post("/extract")
async def extract(file: UploadFile = File(...)):

    upload_path = UPLOAD_FOLDER / file.filename

    with open(upload_path, "wb") as f:
        f.write(await file.read())

    invoice = extract_invoice(upload_path)

    return invoice