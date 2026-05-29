from sqlalchemy.orm import Session

from app.core.infrastructure.database.session import SessionLocal
from app.core.infrastructure.database.repositories.postgres_user_repository import PostgresUserRepository
from app.core.infrastructure.database.repositories.postgres_company_repository import PostgresCompanyRepository

from app.core.domain.entities.user import User
from app.core.domain.enums.role_enum import Role
from app.core.infrastructure.security.password_hasher import PasswordHasher


def run_seed():
    db: Session = SessionLocal()

    user_repo = PostgresUserRepository(db)
    company_repo = PostgresCompanyRepository(db)

    # ⚠️ pega uma company existente (a que você criou agora)
    company = company_repo.get_by_document("422")

    if not company:
        print("Company não encontrada")
        return

    # ⚠️ evita duplicar seed
    existing = user_repo.get_by_email_and_company(
        email="admin@atlas.com",
        company_id=company.id
    )

    if existing:
        print("Admin já existe")
        return

    user = User(
        name="Admin Atlas",
        email="admin@atlas.com",
        password_hash=PasswordHasher.hash("123456"),
        role=Role.ADMIN,
        company_id=company.id
    )

    user_repo.save(user)

    print("Admin criado com sucesso!")


if __name__ == "__main__":
    run_seed()