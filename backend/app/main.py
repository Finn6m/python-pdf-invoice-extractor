from pathlib import Path
from fastapi import FastAPI, UploadFile, File

from fastapi.middleware.cors import CORSMiddleware

from app.services.extractor import extract_invoice

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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