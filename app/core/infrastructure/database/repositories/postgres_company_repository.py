from uuid import UUID
from typing import Optional
from sqlalchemy.orm import Session

from app.core.domain.entities.company import Company
from app.core.domain.services.company_repository import CompanyRepository
from app.core.infrastructure.database.models.company_model import CompanyModel


class PostgresCompanyRepository(CompanyRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, company: Company) -> None:
        model = CompanyModel(
            id=company.id,
            name=company.name,
            document=company.document
        )
        self.db.add(model)
        self.db.commit()

    def get_by_id(self, company_id: UUID) -> Optional[Company]:
        model = self.db.query(CompanyModel).filter_by(id=company_id).first()
        if not model:
            return None

        return Company(
            id=model.id,
            name=model.name,
            document=model.document
        )

    def get_by_document(self, document: str) -> Optional[Company]:
        model = self.db.query(CompanyModel).filter_by(document=document).first()
        if not model:
            return None

        return Company(
            id=model.id,
            name=model.name,
            document=model.document
        )