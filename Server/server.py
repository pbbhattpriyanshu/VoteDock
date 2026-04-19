from fastapi import FastAPI

app = FastAPI()

# Root route
@app.get("/")
def home():
    return {"message": "Welcome to the Voting System API 🚀"}