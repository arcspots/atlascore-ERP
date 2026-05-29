from app.core.infrastructure.database.database import engine, Base
from app.core.infrastructure.database.models import *


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!")