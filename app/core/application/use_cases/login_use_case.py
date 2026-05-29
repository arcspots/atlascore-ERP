from app.core.domain.entities import user
from app.core.infrastructure.security.password_hasher import PasswordHasher
from app.core.infrastructure.security.jwt_service import JWTService


class InvalidCredentials(Exception):
    pass


class LoginUseCase:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str, company_id: str):

        user = self.user_repository.get_by_email_and_company(
            email=email,
            company_id=company_id
        )

        if not user:
            raise InvalidCredentials()

        if not PasswordHasher.verify(password, user.password_hash):
            raise InvalidCredentials()

        token = JWTService.create_access_token({
            "sub": str(user.id),
            "role": user.role.value,
            "company_id": str(user.company_id)
        })

        return token