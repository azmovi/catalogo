import uuid
from datetime import date
from typing import Annotated

from pydantic import BaseModel, BeforeValidator

# def validate_birthday(birthday: str, date_format: str = "%Y-%m-%d") -> str:
#     if not datetime.strptime(birthday, date_format):
#         raise ValueError('Invalid birthday')
#     return birthday


def validate_stack(stack: list[str], max_length=32) -> list[str]:
    for tec in stack:
        if len(tec) >= max_length:
            raise ValueError('stack max length error')
    return stack


class SchemaPerson(BaseModel):
    nick: str
    name: str
    birthday: date
    stack: Annotated[list[str] | None, BeforeValidator(validate_stack)]
    # birthday: Annotated[date, BeforeValidator(validate_birthday)]


class PublicPerson(SchemaPerson):
    id: uuid.UUID
