from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional
from app.core.domain.entities.user import User


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_email_and_company(
        self,
        email: str,
        company_id: UUID
    ) -> Optional[User]:
        pass