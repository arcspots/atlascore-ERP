from uuid import UUID
from typing import Optional
from app.core.domain.entities.company import Company # type: ignore
from app.core.domain.services.company_repository import CompanyRepository # type: ignore


class InMemoryCompanyRepository(CompanyRepository):

    def __init__(self):
        self._companies: dict[UUID, Company] = {}

    def save(self, company: Company) -> None:
        self._companies[company.id] = company

    def get_by_id(self, company_id: UUID) -> Optional[Company]:
        return self._companies.get(company_id)

    def get_by_document(self, document: str) -> Optional[Company]:
        for company in self._companies.values():
            if company.document == document:
                return company
        return None