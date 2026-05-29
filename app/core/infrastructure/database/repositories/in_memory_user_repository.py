from uuid import UUID
from typing import Optional
from app.core.domain.entities.user import User
from app.core.domain.services.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self._users: dict[UUID, User] = {}

    def save(self, user: User) -> None:
        self._users[user.id] = user

    def get_by_email_and_company(
        self,
        email: str,
        company_id: UUID
    ) -> Optional[User]:

        for user in self._users.values():
            if user.email == email and user.company_id == company_id:
                return user

        return None