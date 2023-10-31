from fastapi import APIRouter
from pydantic import BaseModel
from models import Users

router = APIRouter()


class UserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    hashed_password: str
    role: str


@router.get("/auth/")
async def get_user(user_request: UserRequest):
    user_model = Users(**user_request.model_dump())
