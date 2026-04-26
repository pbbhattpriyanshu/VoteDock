from beanie import Document
from pydantic import EmailStr
from typing import Optional
from datetime import datetime

class User(Document):
    name: str
    age: int
    email: Optional[EmailStr]
    phone: str
    address: str
    adharNumber: int
    password: str
    role: str = "voter"
    isVoted: bool = False

    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

    class Settings:
        name = "users"  # collection name