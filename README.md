# 🚀 Programming Language Detector

An AI-powered Programming Language Detection web application built using **Machine Learning**, **FastAPI**, and **HTML/CSS/JavaScript**.  
The application allows users to paste source code or upload code files and automatically predicts the programming language with a confidence score.

---

# 🌐 Live Features

✅ Detect programming languages from pasted code  
✅ Upload source code files (`.py`, `.cpp`, `.java`, etc.)  
✅ Confidence score prediction  
✅ FastAPI backend API  
✅ Modern dark-themed UI  
✅ Machine Learning-based prediction engine  

---

# 🧠 How It Works

The system works in three major stages:

## 1. Frontend
The frontend interface is built using:
- HTML
- CSS
- JavaScript

Users can:
- Paste source code
- Upload source code files
- Send code to backend for prediction

The frontend communicates with the backend using HTTP POST requests via the `fetch()` API.

---

## 2. Backend (FastAPI)

The backend is built using **FastAPI**.

Responsibilities:
- Receive uploaded files or pasted code
- Process user input
- Load trained ML model
- Convert code into numerical vectors
- Predict programming language
- Return JSON response to frontend

---

## 3. Machine Learning Model

The ML model is trained using:
- **TF-IDF Vectorization**
- **Character N-Grams**
- **Logistic Regression**

The vectorizer converts source code into numerical features by analyzing character patterns commonly associated with different programming languages.

Examples:
- `def`, `print` → Python
- `#include`, `cout` → C++
- `console.log` → JavaScript
- `public static void` → Java

The trained model then predicts the most likely language.

---

# ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API framework |
| Scikit-learn | Machine learning |
| HTML/CSS/JS | Frontend |
| Pickle | Model serialization |
| Uvicorn | ASGI server |

---

# 📂 Project Structure

```text
Language Detector/
 ├── app.py
 ├── train.py
 ├── model.pkl
 ├── vectorizer.pkl
 ├── requirements.txt
 └── templates/
      └── index.html
```

---

# ⚡ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/language-detector.git
cd language-detector
```

---

## 2. Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Train Model

```bash
python train.py
```

This generates:
- `model.pkl`
- `vectorizer.pkl`

---

## 5. Run Application

```bash
python -m uvicorn app:app --reload
```

Open:
```text
http://127.0.0.1:8000
```

---

# 🧪 Example Test Inputs

## Python
```python
def hello():
    print("Hello")
```

## C++
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello";
}
```

## JavaScript
```javascript
console.log("Hello");
```

---

# 🧠 Machine Learning Pipeline

```text
User Input
     ↓
Frontend
     ↓
FastAPI Backend
     ↓
TF-IDF Vectorizer
     ↓
Logistic Regression Model
     ↓
Prediction + Confidence
     ↓
Frontend Display
```

---

# 📈 Future Improvements

- Transformer-based models (CodeBERT)
- More programming language support
- Syntax highlighting
- Multi-language file detection
- Top 3 prediction probabilities
- Improved UI/UX
- Docker deployment
- Cloud deployment scaling

---

# 🎯 Learning Outcomes

This project demonstrates concepts in:
- Machine Learning
- NLP-based text classification
- API development
- Backend engineering
- Frontend-backend communication
- Model deployment
- Software architecture

---

# 🏆 Why This Project Matters

Programming language detection is used in:
- Syntax highlighters
- Code editors
- AI coding assistants
- Code analysis systems
- Developer tools
- Educational platforms

This project combines Machine Learning and Full Stack Development into a practical real-world application.

---

# 👨‍💻 Author

**Shreyan Dey**

B.Tech Electronics & Communication Engineering  
Techno India University  



# 📜 License

This project is licensed under the MIT License.
