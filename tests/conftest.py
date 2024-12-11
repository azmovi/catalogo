import pytest
import factory
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy.engine import create_engine
from sqlmodel import Session, SQLModel, create_engine
from testcontainers.postgres import PostgresContainer

from catalogo.app import app
from catalogo.database import get_session, database_url
from catalogo.model import Person
from tests.factories import FactoryPerson

@pytest.fixture(scope='session')
def engine():
    with PostgresContainer('postgres:latest', driver='psycopg') as postgres:
        _engine = create_engine(postgres.get_connection_url())
        with _engine.begin():
            yield _engine

@pytest.fixture(scope='session')
def session(engine):
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    SQLModel.metadata.drop_all(engine)


@pytest.fixture(name='client')
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture(autouse=True)
def configure_factories(session):
    factories = factory.alchemy.SQLAlchemyModelFactory.__subclasses__()
    for fac in factories:
        fac._meta.sqlalchemy_session = session # type: ignore
