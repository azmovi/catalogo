from dataclasses import asdict
from tests.factories import FactoryPerson

from sqlalchemy import select
from sqlalchemy.orm import Session

from catalogo.model import Person


def test_create_user(session: Session):
    print(FactoryPerson())
    print(FactoryPerson.create())
    print(session.scalar(select(Person)))
    assert None == False
