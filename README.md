# Secure Internal Chatbot System – Prototype

## Team Members
- **Yisakor Mirany** – Frontend UI & Integration  
- **[Teammate 2 Name]** – Backend & Security  
- **[Teammate 3 Name]** – System Architecture & Documentation  

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

    A[User Browser] --> B[Frontend (HTML/CSS/JS)]
    B -->|POST /chat\nToken + Question| C[FastAPI Backend]
    C -->|Validate Token| D{Token Valid?}

    D -- Yes --> E[Generate Local Response]
    D -- No --> F[Return 401 Unauthorized]

    E --> G[Send JSON Response]
    F --> G

    G --> H[Frontend Displays Output]
