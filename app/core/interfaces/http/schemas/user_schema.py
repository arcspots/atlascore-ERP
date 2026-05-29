from pydantic import BaseModel, EmailStr
from uuid import UUID
from app.core.domain.enums.role_enum import Role


class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Role
    company_id: UUID