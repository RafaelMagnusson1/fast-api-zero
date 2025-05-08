from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

# Cada classe registrada pelo objeto registry é
# automaticamente mapeada para uma tabela no DB

"""

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int]
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    created_at: Mapped[datetime]

# Mapped refere-se a um atributo associado a
# uma coluna específica do DB
"""


# Melhorando a tabela user

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )


# unique -> campo só pode ter um valor único na tabela
# server_default -> executa uma função no momento
# em que o objeto for instanciado


# int = False -> Atributo não deve ser passado
#  no momento que User intanciado
