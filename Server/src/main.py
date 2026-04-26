from fastapi import FastAPI
from src.database.mongoDB import connect_db, close_db
from src.api import auth

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_db():
    await close_db()

# Root route
@app.get("/")
def home():
    return {"message": "Welcome to the Voting System API 🚀"}

# additional Routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])