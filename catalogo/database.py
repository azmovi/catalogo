from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

database_url = (
    "postgresql+psycopg://app_user:app_password@catalogo_database:5432/app_db"
)
engine = create_engine(database_url)


def get_session():  # pragma: no cover
    with Session(engine) as session:
        yield session


SessionT = Annotated[Session, Depends(get_session)]
