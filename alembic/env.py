from logging.config import fileConfig
import os

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Config do Alembic
config = context.config

# Faz o Alembic usar a mesma DATABASE_URL do projeto
database_url = os.getenv("DATABASE_URL")
config.set_main_option("sqlalchemy.url", database_url)

# Configura logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 🔥 IMPORTANTE: conectar sua Base
from app.core.infrastructure.database.database import Base
# IMPORTAR TODOS OS MODELS AQUI
from app.core.infrastructure.database.models.user_model import UserModel
from app.core.infrastructure.database.models.company_model import CompanyModel
# Aqui o Alembic enxerga os models
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Modo offline"""
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Modo online"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()