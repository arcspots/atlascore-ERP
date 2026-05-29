from app.core.application.use_cases.create_company_use_case import CreateCompanyUseCase
from app.core.application.use_cases.create_user_use_case import CreateUserUseCase

from app.core.infrastructure.database.repositories.in_memory_company_repository import InMemoryCompanyRepository
from app.core.infrastructure.database.repositories.in_memory_user_repository import InMemoryUserRepository  # type: ignore

from app.core.infrastructure.security.password_hasher import PasswordHasher

from app.core.domain.entities.user import User
from app.core.domain.enums.role_enum import Role


# Repositories
company_repository = InMemoryCompanyRepository()
user_repository = InMemoryUserRepository()


# Use cases
create_company = CreateCompanyUseCase(company_repository)

create_user = CreateUserUseCase(
    user_repository,
    company_repository
)


# 1️⃣ Criar empresa
company = create_company.execute(
    name="Atlas Corp",
    document="123456789"
)

print("Company created:", company.id)


# 2️⃣ Criar admin manualmente (bootstrap do sistema)

admin_password_hash = PasswordHasher().hash("123456")

admin_user = User(
    name="Admin",
    email="admin@atlas.com",
    password_hash=admin_password_hash,
    role=Role.ADMIN,
    company_id=company.id
)

user_repository.save(admin_user)

print("Admin created:", admin_user.id)


# 3️⃣ Admin cria usuário normal

new_user = create_user.execute(
    name="John",
    email="john@atlas.com",
    password="123456",
    role=Role.USER,
    company_id=company.id,
    creator_role=admin_user.role
)

print("User created:", new_user.id)


# 4️⃣ Usuário normal tentando criar outro usuário (deve falhar)

try:

    create_user.execute(
        name="Hacker",
        email="hack@atlas.com",
        password="123456",
        role=Role.USER,
        company_id=company.id,
        creator_role=new_user.role
    )

except Exception as e:
    print("Expected error:", e)