import uvicorn
from fastapi import FastAPI, UploadFile, File, Form
from backend.file_processor import extract_text_from_pdf, extract_text_from_image, extract_data_from_csv, extract_data_from_excel, extract_text_from_docx, extract_text_from_txt
from backend.query_handler import query_deepseek
from backend.visualization import plot_data
import pandas as pd
import shutil
import os
import mimetypes

app = FastAPI()

# Create temp directory if it doesn't exist
TEMP_DIR = "backend/temp_files"
os.makedirs(TEMP_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Server is running!"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_ext = file.filename.split(".")[-1].lower()
    mime_type, _ = mimetypes.guess_type(file.filename)

    # Debugging log
    print(f"Uploaded file: {file.filename}, Extension: {file_ext}, MIME Type: {mime_type}")

    file_path = os.path.join(TEMP_DIR, file.filename)

    # Save file to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process text-based files
    if mime_type == "application/pdf" or file_ext == "pdf":
        text = extract_text_from_pdf(file_path)
        return {"message": "PDF processed", "content": text[:500]}

    elif file_ext in ["txt"]:
        text = extract_text_from_txt(file_path)
        return {"message": "TXT processed", "content": text[:500]}

    elif file_ext in ["docx"]:
        text = extract_text_from_docx(file_path)
        return {"message": "DOCX processed", "content": text[:500]}

    # Process structured data (CSV, Excel)
    elif file_ext == "csv":
        df = extract_data_from_csv(file_path)
        return {"message": "CSV processed", "data_preview": df.head().to_dict()}

    elif file_ext in ["xlsx", "xls"]:
        df = extract_data_from_excel(file_path)
        return {"message": "Excel processed", "data_preview": df.head().to_dict()}

    # Process image files
    elif file_ext in ["png", "jpg", "jpeg"]:
        text = extract_text_from_image(file_path)
        return {"message": "Image processed", "content": text[:500]}

    else:
        return {"error": "Unsupported file format"}

@app.post("/analyze/")
async def analyze_text(question: str = Form(...), text: str = Form(...)):
    response = query_deepseek(f"Analyze this text and answer the question: {text[:1000]} \n\n Question: {question}")
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
