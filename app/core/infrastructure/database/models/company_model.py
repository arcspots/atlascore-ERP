from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.core.infrastructure.database.database import Base
import uuid


class CompanyModel(Base):
    __tablename__ = "companies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    document = Column(String, nullable=False, unique=True)