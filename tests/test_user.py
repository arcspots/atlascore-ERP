import pytest

from app.core.application.use_cases.create_company_use_case import CreateCompanyUseCase

from app.core.application.use_cases.create_user_use_case import (
    CreateUserUseCase,
    PermissionDenied
)

from app.core.infrastructure.database.repositories.in_memory_company_repository import InMemoryCompanyRepository

from app.core.infrastructure.database.repositories.in_memory_user_repository import InMemoryUserRepository

from app.core.infrastructure.security.password_hasher import PasswordHasher

from app.core.domain.entities.user import User
from app.core.domain.enums.role_enum import Role


def setup_environment():

    company_repo = InMemoryCompanyRepository()
    user_repo = InMemoryUserRepository()

    create_company = CreateCompanyUseCase(company_repo)

    create_user = CreateUserUseCase(
        user_repo,
        company_repo
    )

    company = create_company.execute(
        "Atlas Corp",
        "123456789"
    )

    admin_password_hash = PasswordHasher().hash("123456")

    admin = User(
        name="Admin",
        email="admin@atlas.com",
        password_hash=admin_password_hash,
        role=Role.ADMIN,
        company_id=company.id
    )

    user_repo.save(admin)

    return create_user, admin, user_repo, company


def test_admin_can_create_user():

    create_user, admin, user_repo, company = setup_environment()

    new_user = create_user.execute(
        name="John",
        email="john@atlas.com",
        password="123456",
        role=Role.USER,
        company_id=company.id,
        creator_role=admin.role
    )

    assert new_user.email == "john@atlas.com"
    assert new_user.role == Role.USER


def test_non_admin_cannot_create_user():

    create_user, admin, user_repo, company = setup_environment()

    normal_user = create_user.execute(
        name="John",
        email="john@atlas.com",
        password="123456",
        role=Role.USER,
        company_id=company.id,
        creator_role=admin.role
    )

    with pytest.raises(PermissionDenied):

        create_user.execute(
            name="Hacker",
            email="hack@atlas.com",
            password="123456",
            role=Role.USER,
            company_id=company.id,
            creator_role=normal_user.role
        )