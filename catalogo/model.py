from typing import Annotated
import uuid
from datetime import datetime

from pydantic import BeforeValidator
from sqlalchemy import JSON, Column, String
from sqlmodel import Field, SQLModel

def validate_birthday(birthday: str, date_format: str = "%Y-%m-%d") -> str:
    if not datetime.strptime(birthday, date_format):
        raise ValueError('Invalid birthday')
    return birthday


def validate_stack(stack: list[str], max_length=32) -> list[str]:
    for tec in stack:
        if len(tec) >= max_length:
            raise ValueError('stack max length error')
    return stack

class Person(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    #nick: str = Field(max_length=32, index=True)
    nick: str = Field(sa_column=Column(String(32), index=True))
    name: str = Field(max_length=100)
    birthday: Annotated[str, BeforeValidator(validate_birthday)]
    stack: Annotated[
        list[str] | None, BeforeValidator(validate_stack)
    ] = Field(sa_column=Column(JSON))
