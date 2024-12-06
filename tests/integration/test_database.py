from sqlalchemy import select
from sqlalchemy.orm import Session

from catalogo.model import Person
from tests.factories import FactoryPerson


def test_many_person_for_one_product(session: Session):
    FactoryPerson.create_batch(3)
    people = session.scalar(select(Person))
    print(people)
    # assert None == False
