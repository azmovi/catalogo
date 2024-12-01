from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

sqlite_url = 'sqlite:///./db.sqlite3'
engine = create_engine(sqlite_url)


def get_session():  # pragma: no cover
    with Session(engine) as session:
        yield session


SessionT = Annotated[Session, Depends(get_session)]
