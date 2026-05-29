from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.infrastructure.database.session import get_db
from app.core.infrastructure.database.repositories.postgres_user_repository import PostgresUserRepository
from app.core.infrastructure.database.repositories.postgres_company_repository import PostgresCompanyRepository
from app.core.infrastructure.database.models.user_model import UserModel
from app.core.infrastructure.security.dependencies import get_current_user

from app.core.application.use_cases.create_user_use_case import CreateUserUseCase
from app.core.interfaces.http.schemas.user_schema import CreateUserRequest


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(
    request: CreateUserRequest,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """
    Apenas ADMIN pode criar usuários.
    Usuário só pode criar dentro da própria empresa.
    """

    #  Verifica se é ADMIN
    if current_user.role != "ADMIN":
        raise HTTPException(
            status_code=403,
            detail="Only ADMIN can create users"
        )

    # 🔐 Impede criar usuário em outra empresa
    if str(current_user.company_id) != str(request.company_id):
        raise HTTPException(
            status_code=403,
            detail="Cannot create user in another company"
        )

    user_repository = PostgresUserRepository(db)
    company_repository = PostgresCompanyRepository(db)

    use_case = CreateUserUseCase(
        user_repository=user_repository,
        company_repository=company_repository
    )

    user = use_case.execute(
        name=request.name,
        email=request.email,
        password=request.password,
        role=request.role,
        company_id=request.company_id,
        creator_role=current_user.role  #  vem do token
    )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "company_id": user.company_id
    }