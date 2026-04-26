from fastapi import APIRouter

router = APIRouter()

@router.get("/signup")
def test_auth():
    return {"message": "App Route is working"}