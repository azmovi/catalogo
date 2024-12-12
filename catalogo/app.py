from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from sqlalchemy import Select, String, cast, select
from sqlalchemy.exc import DataError, IntegrityError

from catalogo.database import SessionT
from catalogo.model import Person

app = FastAPI()


@app.post(
    '/people/',
    summary='Create People',
    status_code=HTTPStatus.CREATED,
    response_model=Person
)
def create_person(person: Person, session: SessionT):
    try:
        stmt = select(Person).where(
            cast(Person.name, String) == person.name
        )
        if session.scalar(stmt):
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='nick alredy in database',
            )
        session.add(person)
        session.commit()
        session.refresh(person)
        return person

    except IntegrityError:
        session.rollback()

        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Database integrity error',
        )

    except DataError:
        session.rollback()

        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Invalid content in field',
        )


@app.get(
    '/people/{nick}/',
    summary='Get People by nick',
    status_code=HTTPStatus.OK,
    response_model=Person
)
def get_person(nick: str, session: SessionT):
    if person := session.scalars(
        Select(Person).filter_by(nick=nick)
    ).one_or_none():
        return person

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail='Person not found'
    )
