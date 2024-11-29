from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, Session

sqlite_url = 'sqlite:///./db.sqlite3'
engine = create_engine(sqlite_url)


def get_session():  # pragma: no cover
    with Session(engine) as session:
        yield session


SessionT = Annotated[Session, Depends(get_session)]
