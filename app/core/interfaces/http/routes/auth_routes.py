from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from app.core.infrastructure.database.session import get_db
from app.core.infrastructure.database.repositories.postgres_user_repository import PostgresUserRepository
from app.core.application.use_cases.login_use_case import LoginUseCase, InvalidCredentials


router = APIRouter(prefix="/auth", tags=["Auth"])


class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    company_id: str


@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):

    repository = PostgresUserRepository(db)
    use_case = LoginUseCase(repository)

    try:
        token = use_case.execute(
            request.email,
            request.password,
            request.company_id
        )

        return {"access_token": token}

    except InvalidCredentials:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )