from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.core.infrastructure.database.session import get_db
from app.core.infrastructure.database.repositories.postgres_company_repository import PostgresCompanyRepository
from app.core.application.use_cases.create_company_use_case import CreateCompanyUseCase
from app.core.interfaces.http.schemas.company_schema import CreateCompanyRequest

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.post("/")
def create_company(request: CreateCompanyRequest, db: Session = Depends(get_db)):
    repository = PostgresCompanyRepository(db)
    use_case = CreateCompanyUseCase(repository)

    company = use_case.execute(
        name=request.name,
        document=request.document
    )

    return {
        "id": company.id,
        "name": company.name,
        "document": company.document
    }