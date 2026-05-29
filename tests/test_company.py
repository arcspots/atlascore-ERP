import pytest
from app.core.application.use_cases.create_company_use_case import CreateCompanyUseCase
from app.core.infrastructure.database.repositories.in_memory_company_repository import InMemoryCompanyRepository
from app.core.domain.exceptions.domain_exceptions import CompanyAlreadyExists


def test_create_company_success():
    repository = InMemoryCompanyRepository()
    use_case = CreateCompanyUseCase(repository)

    company = use_case.execute("Atlas Corp", "123456789")

    assert company.name == "Atlas Corp"
    assert company.document == "123456789"


def test_create_company_duplicate_document():
    repository = InMemoryCompanyRepository()
    use_case = CreateCompanyUseCase(repository)

    use_case.execute("Atlas Corp", "123456789")

    with pytest.raises(CompanyAlreadyExists):
        use_case.execute("Another Corp", "123456789")