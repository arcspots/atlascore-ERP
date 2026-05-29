from app.core.domain.entities.company import Company
from app.core.domain.services.company_repository import CompanyRepository
from app.core.domain.exceptions.domain_exceptions import CompanyAlreadyExists


class CreateCompanyUseCase:

    def __init__(self, company_repository: CompanyRepository):
        self.company_repository = company_repository

    def execute(self, name: str, document: str) -> Company:
        existing_company = self.company_repository.get_by_document(document)

        if existing_company:
            raise CompanyAlreadyExists("Company with this document already exists")

        company = Company(name=name, document=document)

        self.company_repository.save(company)

        return company