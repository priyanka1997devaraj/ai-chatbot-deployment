from fastapi import FastAPI

app = FastAPI()

@app.get("/chat")
def chat(message: str):
    # Replace with AI model logic later
    return {"response": f"You said: {message}"}
