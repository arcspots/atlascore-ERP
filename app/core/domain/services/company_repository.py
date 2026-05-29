from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional
from app.core.domain.entities.company import Company


class CompanyRepository(ABC):

    @abstractmethod
    def save(self, company: Company) -> None:
        pass

    @abstractmethod
    def get_by_id(self, company_id: UUID) -> Optional[Company]:
        pass

    @abstractmethod
    def get_by_document(self, document: str) -> Optional[Company]:
        pass