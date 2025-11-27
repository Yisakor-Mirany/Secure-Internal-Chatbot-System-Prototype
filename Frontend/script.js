// Frontend script for Secure Internal Chatbot Prototype

document.getElementById("sendBtn").addEventListener("click", async () => {
    const token = document.getElementById("token").value.trim();
    const question = document.getElementById("question").value.trim();
    const errorMessage = document.getElementById("errorMessage");
    const responseBox = document.getElementById("responseBox");

    // Clear previous messages
    errorMessage.textContent = "";
    
    if (!token || !question) {
        errorMessage.textContent = "Please enter both token and question.";
        return;
    }

    try {
        const res = await fetch("http://localhost:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": token
            },
            body: JSON.stringify({ question })
        });

        if (res.status === 401) {
            errorMessage.textContent = "Invalid token. Access denied.";
            return;
        }

        if (!res.ok) {
            errorMessage.textContent = "Server error. Try again.";
            return;
        }

        const data = await res.json();
        responseBox.textContent = data.answer;

    } catch (err) {
        errorMessage.textContent = "Unable to connect to backend.";
        console.error(err);
    }
});
