from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=50)
    full_name: str = Field(min_length=3, max_length=100)
    phone: str | None = Field(min_length=5, max_length=20)
    email_verified: bool = Field(default=False)
    is_active: bool = Field(default=False)
