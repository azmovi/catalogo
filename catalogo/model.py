from __future__ import annotations
import uuid
from typing import List, Optional

from sqlalchemy import JSON, Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship, registry

table_registry = registry()


people_products = Table(
    "people_products",
    table_registry.metadata,
    Column("person_id", ForeignKey("people.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True),
)


@table_registry.mapped_as_dataclass
class Person:
    __tablename__ = 'people'

    id: Mapped[uuid.UUID] = mapped_column(
        init=False, primary_key=True, default_factory=uuid.uuid4
    )
    nick: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    birthday: Mapped[str]
    stack: Mapped[list[str] | None] = mapped_column(JSON)
    products: Mapped[Optional[List[Product]]] = relationship(
        secondary=people_products,
        back_populates='people',
    )


@table_registry.mapped_as_dataclass
class Product:
    __tablename__ = 'products'

    id: Mapped[uuid.UUID] = mapped_column(
        init=False, primary_key=True, default_factory=uuid.uuid4
    )
    nome: Mapped[str] = mapped_column(unique=True, index=True)
    people: Mapped[Optional[List[Person]]] = relationship(
        secondary=people_products,
        back_populates='products',
    )
