
# 🚀 FastAPI with Uvicorn

This project demonstrates how to run a FastAPI application using a Python virtual environment (`venv`) and `uvicorn`.

---

## 📦 Requirements

- Python 3.11+
- Git (optional)

---

## 🛠 Setup Instructions

### 1. Clone the repository (optional)

```bash
git clone https://github.com/engineering-of-zylosystems/user-server-1
cd user-server-1
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

- **Windows (CMD):**
  ```cmd
  venv\Scripts\activate
  ```

- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can install manually:

```bash
pip install fastapi uvicorn
```

---

## 🚀 Running the App

```bash
uvicorn main:app --reload
```

- `main` is the Python file (e.g., `main.py`)
- `app` is the FastAPI instance: `app = FastAPI()`
- `--reload` enables auto-reload for development

Then open: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📄 Example `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

---

## 🧹 Deactivate the venv

When you're done, run:

```bash
deactivate
```

---

## 📌 Notes

- To freeze dependencies:
  ```bash
  pip freeze > requirements.txt
  ```

- To install from `requirements.txt` again:
  ```bash
  pip install -r requirements.txt
  ```
