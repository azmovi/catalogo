from sqlalchemy import select
from sqlalchemy.orm import Session

from catalogo.model import Person
from tests.factories import FactoryPerson


def test_person_model(session: Session):
    person = FactoryPerson.create()
    people = session.scalar(select(Person).filter(Person.id == person.id))
    assert person == people
