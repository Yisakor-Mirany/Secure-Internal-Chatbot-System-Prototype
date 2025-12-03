# Secure Internal Chatbot System – Prototype

## Team Members
- **Yisakor Mirany** – Frontend UI & Integration  
- **Lindokuhle Ngobese** – Backend & Security  
- **Asma Begum** – System Architecture & Documentation  

---

## 📌 Project Overview
This prototype is part of the *Real World Project: Designing a Secure, In-House Chatbot System*.  
The goal is to demonstrate a **minimal, secure, locally hosted chatbot interaction** — proving technical feasibility for a fully private, in-house AI assistant.

This demo focuses on:
- Local-only architecture  
- Secure token-based authentication  
- Simple frontend + backend integration  
- Zero external API calls  

---

## 🔐 Key Security Feature Demonstrated
### **Secure Token Authentication**
All requests must include a valid token in the `Authorization` header.

- ✔ Prevents unauthorized access  
- ✔ Demonstrates access control  
- ✔ Shows how internal systems verify identity  
- ✔ Ensures only approved employees can use the chatbot  

Invalid tokens return a **401 Unauthorized** error.

---

## 🏗 Technology Stack

### **Frontend**
- HTML  
- CSS  
- JavaScript (fetch API)  

### **Backend**
- Python  
- FastAPI  
- Uvicorn  

### **Security**
- Token-based authentication  
- Input validation  
- Fully local response generation  

---

## 🚀 Prototype Features
- ✔ Secure token input  
- ✔ Local-only chatbot responses  
- ✔ Clear error messages for invalid tokens or missing inputs  
- ✔ Simple, clean UI for testing  

---

## 🚀 How to Run the Prototype
1. Clone the Repository
   git clone https://github.com/Yisakor-Mirany/Secure-Internal-Chatbot-System-Prototype.git
   cd Secure-Internal-Chatbot-System-Prototype

2. Install Backend Dependencies
   Make sure you have Python 3.10+ installed.
   - pip install -r requirements.txt

3. Start the Backend Server
   - uvicorn main:app --reload
  Backend will run at:
   - http://127.0.0.1:8000

4. Open the Frontend
   - Open index.html in your browser

5. Use the Chatbot
   - Enter your access token
   - Type a question
   - Click Send
 

## 📂 Project Structure
Secure-Internal-Chatbot-Design/
│
├── backend/
│ ├── main.py
│ └── requirements.txt
│
└── frontend/
├── index.html
├── script.js
└── styles.css

---

## 🏗 System Architecture Diagram

```mermaid
flowchart TD

    A[User Browser] --> B[Frontend UI]
    B -->|request| C[FastAPI Backend]
    C -->|check token| D{Valid Token?}

    D -->|yes| E[Generate Response]
    D -->|no| F[Return 401]

    E --> G[Send Response]
    F --> G

    G --> H[Display in UI]
