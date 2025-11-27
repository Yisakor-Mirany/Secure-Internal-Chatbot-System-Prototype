document.getElementById("sendBtn").addEventListener("click", sendMessage);

function addResponse(message) {
    document.getElementById("responseBox").textContent = message;
}

async function sendMessage() {
    const token = document.getElementById("token").value.trim();
    const question = document.getElementById("question").value.trim();
    const errorMessage = document.getElementById("errorMessage");

    errorMessage.textContent = "";
    addResponse("");

    if (!token) {
        errorMessage.textContent = "Access token is required.";
        return;
    }

    if (!question) {
        errorMessage.textContent = "Please enter a question.";
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
            errorMessage.textContent = "Server error.";
            return;
        }

        const data = await res.json();
        addResponse(data.answer);

    } catch (err) {
        errorMessage.textContent = "Could not connect to backend.";
        console.error(err);
    }
}
