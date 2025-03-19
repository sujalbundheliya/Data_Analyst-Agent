import pdfplumber
import pytesseract
import cv2
import pandas as pd
import docx
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text

def extract_data_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    return df

def extract_data_from_excel(excel_path):
    df = pd.read_excel(excel_path)
    return df

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join([p.text for p in doc.paragraphs])
    return text

def extract_text_from_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text
