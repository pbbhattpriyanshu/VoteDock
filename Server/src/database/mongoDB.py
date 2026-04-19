from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import MONGO_URL, DB_NAME

client = None
db = None

async def connect_db():
    global client, db
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    print("MongoDB Connected")

async def close_db():
    global client
    if client:
        client.close()
        print("MongoDB Disconnected")