import pytest
import factory
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy.engine import create_engine
from sqlalchemy.pool import StaticPool

from catalogo.app import app
from catalogo.database import get_session
from catalogo.model import table_registry

@pytest.fixture(name='session')
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


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
