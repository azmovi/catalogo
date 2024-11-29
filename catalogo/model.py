import uuid
from datetime import date
from typing import Annotated

from pydantic import AfterValidator
from sqlmodel import Field, SQLModel


def valid_stack(stack: list[str], max_length: int = 32) -> list[str]:
    for tec in stack:
        if len(tec) >= max_length:
            raise ValueError(f'stack max lenght error')
    return stack

class Tecnology(SQLModel, table=False):
    tecnology: str

class Stack(SQLModel, table=False):
    stack: list[Tecnology]

class Person(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    nick: str = Field(max_length=32, unique=True)
    name: str = Field(max_length=100)
    birthday: date
    stack: Annotated[Stack | None, AfterValidator(valid_stack)]

