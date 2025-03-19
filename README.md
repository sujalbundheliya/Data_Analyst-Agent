# 📊 Data Analyst Agent

This is a **FastAPI-based Data Analyst Agent** that allows users to:
- **Upload various document formats** (`.docx`, `.txt`, `.xlsx`, `.csv`, `.pdf`, `.png/.jpg`)
- **Extract data and text** from uploaded files
- **Ask AI-powered questions** using **DeepSeek-R1 (Ollama)**
- **Interact via a Streamlit UI** for ease of use
- **Visualize structured data** (CSV/XLSX)

---

## 📂 **Project Structure**

Data-Analyst-Agent

├── backend 

│   ├── file_processor.py    # Extracts text from various file types 

│   ├── main.py             # FastAPI app

│   ├── query_handler.py    # AI interaction with DeepSeek-R1 via Ollama

│   ├── visualization.py    # Bar & Scatter plots

├── frontend

│   ├── app.py             # Streamlit UI

├── temp_files              # Temporary storage (auto-created)

├── .gitignore             # Git exclusions

├── requirements.txt        # Dependencies

├── README.md              # Docs



---

## 🚀 **Setup & Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/sujalbundheliya/Data_Analyst-Agent.git
cd Data-Analyst-Agent
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Mac/Linux)
venv\Scripts\activate  # Activate (Windows)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install & Run Ollama (DeepSeek-R1)

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download DeepSeek-R1 model
ollama pull deepseek-r1

# Run Ollama
ollama run deepseek-r1
```

### 5️⃣ Start FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

✅ FastAPI runs at: http://127.0.0.1:8000/

✅ API Docs available at: http://127.0.0.1:8000/docs

###6️⃣ Start Streamlit Frontend

```bash
cd frontend
streamlit run app.py
```

✅ Streamlit runs at: http://localhost:8501/


