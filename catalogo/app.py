from http import HTTPStatus
from typing import cast

from fastapi import FastAPI, HTTPException
from sqlalchemy import select, cast, String


from .model import Person 
from .database import SessionT

app = FastAPI()


@app.post(
    '/people',
    summary='Create People',
    status_code=HTTPStatus.CREATED,
    response_model=Person,
)
def create(person: Person, session: SessionT) -> Person:
    stmt = select(Person).where(
        cast(Person.name, String) == person.name
    )
    if session.scalar(stmt):
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='nick alredy in database'
        )
    session.add(person)
    session.commit()
    session.refresh(person)
    return person
