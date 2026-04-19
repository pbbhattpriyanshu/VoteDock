from fastapi import FastAPI
from src.database.mongoDB import connect_db, close_db

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_db():
    await close_db

# Root route
@app.get("/")
def home():
    return {"message": "Welcome to the Voting System API 🚀"}