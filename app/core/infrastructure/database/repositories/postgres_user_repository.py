from uuid import UUID
from typing import Optional
from sqlalchemy.orm import Session

from app.core.domain.entities.user import User
from app.core.domain.services.user_repository import UserRepository
from app.core.domain.enums.role_enum import Role
from app.core.infrastructure.database.models.user_model import UserModel


class PostgresUserRepository(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, user: User) -> None:
        model = UserModel(
            id=user.id,
            name=user.name,
            email=user.email,
            password_hash=user.password_hash,
            role=user.role.value,
            company_id=user.company_id
        )

        self.db.add(model)
        self.db.commit()

    def get_by_email_and_company(
        self,
        email: str,
        company_id: UUID
    ) -> Optional[User]:

        model = (
            self.db.query(UserModel)
            .filter_by(email=email, company_id=company_id)
            .first()
        )

        if not model:
            return None

        return User(
            id=model.id,
            name=model.name,
            email=model.email,
            password_hash=model.password_hash,
            role=Role(model.role),
            company_id=model.company_id
        )

    def get_by_id(self, user_id: UUID) -> Optional[User]:

        model = (
            self.db.query(UserModel)
            .filter_by(id=user_id)
            .first()
        )

        if not model:
            return None

        return User(
            id=model.id,
            name=model.name,
            email=model.email,
            password_hash=model.password_hash,
            role=Role(model.role),
            company_id=model.company_id
        )