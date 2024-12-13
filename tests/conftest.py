from typing import Generator

import factory
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine
from testcontainers.postgres import PostgresContainer

from catalogo.app import app
from catalogo.database import get_session
from catalogo.model import Person
from tests.factories import FactoryPerson


@pytest.fixture(scope='session')
def engine() -> Generator[Engine]:
    with PostgresContainer('postgres:latest', driver='psycopg') as postgres:
        _engine = create_engine(postgres.get_connection_url())
        with _engine.begin():
            yield _engine


@pytest.fixture(scope='session')
def session(engine) -> Generator[Session]:
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    SQLModel.metadata.drop_all(engine)


@pytest.fixture(name='client')
def client(session) -> Generator[TestClient]:
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture(autouse=True)
def configure_factories(session) -> None:
    factories = factory.alchemy.SQLAlchemyModelFactory.__subclasses__()
    for fac in factories:
        fac._meta.sqlalchemy_session = session  # type: ignore


@pytest.fixture(name='person')
def person() -> Person:
    person = FactoryPerson.create()
    return person
