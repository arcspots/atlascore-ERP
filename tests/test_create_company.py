from app.core.application.use_cases.create_company_use_case import CreateCompanyUseCase # type: ignore
from app.core.infrastructure.database.repositories.in_memory_company_repository import InMemoryCompanyRepository


repository = InMemoryCompanyRepository()
use_case = CreateCompanyUseCase(repository)

company = use_case.execute(
    name="Atlas Corp",
    document="123456789"
)

print("Company created:")
print(company.id, company.name, company.document)