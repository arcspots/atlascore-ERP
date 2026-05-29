from uuid import uuid4, UUID
from app.core.domain.enums.role_enum import Role


class User:

    def __init__(
        self,
        name: str,
        email: str,
        password_hash: str,
        role: Role,
        company_id: UUID,
        id: UUID | None = None
    ):
        if not name:
            raise ValueError("User name cannot be empty")

        if not email:
            raise ValueError("User email cannot be empty")

        if not password_hash:
            raise ValueError("Password hash cannot be empty")

        self.id: UUID = id or uuid4()
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.company_id = company_id