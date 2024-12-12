import uuid
from datetime import date

from sqlalchemy import Column, String
from sqlmodel import ARRAY, Field, SQLModel


class Person(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    nick: str = Field(sa_column=Column(String(32), index=True, nullable=False))
    name: str = Field(max_length=100, nullable=False)
    birthday: date = Field(nullable=False)
    stack: list[str] | None = Field(sa_column=Column(ARRAY(String)))
