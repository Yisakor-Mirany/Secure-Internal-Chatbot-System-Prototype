from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# ---------------------------
# 1. CORS (allows frontend to connect)
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For prototype only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# 2. Secure Token (local-only)
# ---------------------------
SECURE_TOKEN = "12345"   # Example token (you can change)

# ---------------------------
# 3. Chat Endpoint
# ---------------------------
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()

    # Extract question
    question = body.get("question")
    if not question:
        raise HTTPException(status_code=400, detail="Question is required.")

    # Check token from header
    token = request.headers.get("Authorization")
    if token != SECURE_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Local-only response (no external calls)
    answer = f"This is a secure internal response to: '{question}'. (Local-only chatbot prototype)"

    return {"answer": answer}


# ---------------------------
# Run the API
# ---------------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
