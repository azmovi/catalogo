from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from sqlalchemy import String, cast, select
from sqlalchemy.exc import IntegrityError

from catalogo.database import SessionT
from catalogo.model import Person, SchemaPerson

app = FastAPI()


@app.post(
    '/people',
    summary='Create People',
    status_code=HTTPStatus.CREATED,
    response_model=Person
)
def create(person: SchemaPerson, session: SessionT):
    stmt = select(Person).where(
        cast(Person.name, String) == person.name
    )
    if session.scalar(stmt):
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='nick alredy in database'
        )
    try:
        session.add(person)
        session.commit()
        session.refresh(person)
        return person

    except IntegrityError:
        session.rollback()

        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Database integrity error'
        )
