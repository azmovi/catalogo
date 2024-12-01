import uuid
from datetime import date

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class Person:
    __tablename__ = 'people'

    id: Mapped[uuid.UUID] = mapped_column(
        init=False, primary_key=True, default_factory=uuid.uuid4
    )
    nick: Mapped[str] = mapped_column(
        String(32), unique=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    birthday: Mapped[str]
    stack: Mapped[list[str] | None] = mapped_column(JSON)


@table_registry.mapped_as_dataclass
class Test:
    __tablename__ = 'tests'

    id: Mapped[uuid.UUID] = mapped_column(init=False, primary_key=True, default_factory=uuid.uuid4)
