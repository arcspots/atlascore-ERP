from uuid import UUID
from app.core.domain.entities.user import User
from app.core.domain.enums.role_enum import Role
from app.core.infrastructure.security.password_hasher import PasswordHasher


class PermissionDenied(Exception):
    pass


class UserAlreadyExists(Exception):
    pass


class CompanyNotFound(Exception):
    pass


class CreateUserUseCase:

    def __init__(self, user_repository, company_repository):
        self.user_repository = user_repository
        self.company_repository = company_repository
        self.password_hasher = PasswordHasher()

    def execute(
        self,
        name: str,
        email: str,
        password: str,
        role: Role,
        company_id: UUID,
        creator_role: Role
    ) -> User:

        # 1️⃣ Verifica empresa
        company = self.company_repository.get_by_id(company_id)
        if not company:
            raise CompanyNotFound("Company not found")

        # 2️⃣ Verifica permissão
        if creator_role != Role.ADMIN:
            raise PermissionDenied("Only ADMIN can create users")

        # 3️⃣ Verifica duplicidade
        existing_user = self.user_repository.get_by_email_and_company(
            email=email,
            company_id=company_id
        )

        if existing_user:
            raise UserAlreadyExists("User already exists in this company")

        # 4️⃣ Gera hash da senha (agora usando a instância corretamente)
        hashed_password = self.password_hasher.hash(password)

        # 5️⃣ Cria entidade
        new_user = User(
            name=name,
            email=email,
            password_hash=hashed_password,
            role=role,
            company_id=company_id
        )

        # 6️⃣ Salva
        self.user_repository.save(new_user)

        return new_user