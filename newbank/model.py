from typing import Annotated
import uuid
from datetime import date


from pydantic import AfterValidator
from sqlmodel import Field, SQLModel

def valid_stack(stack: list[str], max_length: int = 32) -> list[str]:
    for tec in stack:
        if len(tec) >= max_length:
            raise ValueError(
                f'A string excede o tamanho máximo de {max_length} caracteres.'
            )
    return stack

class Pessoa(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    apelido: str = Field(max_length=32, unique=True)
    nome: str = Field(max_length=100)
    nascimento: date
    stack: Annotated[list[str] | None, AfterValidator(valid_stack)]



