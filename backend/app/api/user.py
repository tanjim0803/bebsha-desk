from fastapi import APIRouter
from app.database.session import SessionDep
from app.schemas.user import UserCreate

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def create_user(db: SessionDep, user: UserCreate):
    return {"new_user": user}
