# 🧠 Full Stack ML Web App with FastAPI & Vite

This is a full-stack machine learning web application that includes:

- 🔙 **Backend**: FastAPI (Python)
- 🎨 **Frontend**: Vite (React or Vue)
- 🤖 **ML Model**: Trained and served via a `.pkl` (pickle) file

---

## 📁 Folder Structure

```
project-root/
│
├── backend/
│   ├── main.py
│   ├── model.pkl
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   └── src/
│       └── ...
│
└── majorFinal.ipynb
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.7+
- Node.js and npm
- pip

---

## 🐍 Backend Setup (FastAPI + Pickle Model)

### 1. Navigate to backend directory
```bash
cd backend
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install required Python packages
```bash
pip install -r requirements.txt
```

### 4. Ensure `model.pkl` exists

Your ML model should already be trained and saved like this:

```python
import pickle
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
```

### 5. Run the FastAPI server
```bash
uvicorn main:app --reload
```

- Runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Example FastAPI CORS setup (in `main.py`)
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data: dict):
    # Extract and process features from `data`
    prediction = model.predict([[data["feature1"], data["feature2"]]])  # Modify based on input shape
    return {"prediction": prediction[0]}
```

---

## 🌐 Frontend Setup (Vite)

### 1. Navigate to frontend directory
```bash
cd frontend
```

### 2. Install dependencies
```bash
npm install
```

### 3. Start development server
```bash
npm run dev
```

- Runs at: [http://localhost:5173](http://localhost:5173)

### Example API Call from Frontend (React)
```javascript
const response = await fetch("http://127.0.0.1:8000/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ feature1: 10, feature2: 5 }),
});
const result = await response.json();
console.log(result.prediction);
```

---

## 🧪 Testing the API Manually
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"feature1": 10, "feature2": 5}'
```

---

## 🛠 Building Frontend for Production

```bash
npm run build
```

This will generate a `dist/` folder that can be deployed or integrated with a backend static file server.

---

## 📦 Requirements File Example (backend/requirements.txt)

```
fastapi
uvicorn
scikit-learn
pydantic
numpy
```

> Add any additional packages based on your model (e.g., pandas, joblib)

---


---
## 🙋‍♂️ Author

Made by [Aishwariya Prasoon and Arpit Kumar]
