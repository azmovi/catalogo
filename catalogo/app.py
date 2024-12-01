from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from sqlalchemy import String, cast, select
from sqlalchemy.exc import IntegrityError

from catalogo.database import SessionT
from catalogo.model import Person
from catalogo.schema import SchemaPerson, PublicPerson

app = FastAPI()


@app.post(
    '/people',
    summary='Create People',
    status_code=HTTPStatus.CREATED,
    response_model=PublicPerson
)
def create(person: SchemaPerson, session: SessionT) -> Person:
    stmt = select(Person).where(
        cast(Person.name, String) == person.name
    )
    if session.scalar(stmt):
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='nick alredy in database'
        )
    try:
        person_db = Person(
            nick=person.nick,
            name=person.name,
            birthday=person.birthday,
            stack=person.stack
        )
        session.add(person_db)
        session.commit()
        session.refresh(person_db)
        return person_db

    except IntegrityError:
        session.rollback()

        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Database integrity error'
        )
