from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# ------------------------------------------------
# CORS setup
# ------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------
# Secure Token
# ------------------------------------------------
SECURE_TOKEN = "12345"

# ------------------------------------------------
# Smart Response Generator
# ------------------------------------------------
def generate_smart_reply(question: str) -> str:
    q = question.lower()

    # Greeting
    if any(word in q for word in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"

    # Name detection
    if "yisakor" in q or "mirany" in q:
        return "Nice to meet you, Yisakor! How can I help you today?"

    # Asking who the bot is
    if "who are you" in q or "what are you" in q:
        return "I’m the Secure Internal Chatbot prototype, designed for safe, local-only interactions."

    # Company-specific example (customize as needed)
    if "internal" in q or "security" in q:
        return "This system is fully secure and runs locally with token-based authentication."

    # Asking about capabilities
    if "what can you do" in q or "help" in q:
        return (
            "I can respond to basic questions, identify greetings, "
            "recognize your name, and simulate secure internal support."
        )

    # Fallback generic response
    return (
        f"I received your question: '{question}'. "
        "This is a locally processed response from the internal chatbot prototype."
    )

# ------------------------------------------------
# Chat Endpoint
# ------------------------------------------------
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()

    # Extract question
    question = body.get("question")
    if not question:
        raise HTTPException(status_code=400, detail="Question is required.")

    # Check token
    token = request.headers.get("Authorization")
    if token != SECURE_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Generate smart reply
    answer = generate_smart_reply(question)

    return {"answer": answer}

# ------------------------------------------------
# Run server
# ------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
