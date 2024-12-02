from sqlalchemy import select
from sqlalchemy.orm import Session

from catalogo.model import Product, Person
from tests.factories import FactoryPerson, FactoryProduct


def test_many_person_for_one_product(session: Session):
    people = FactoryPerson.create_batch(3)
    product = FactoryProduct.build()
    product.people.extend(people)
    session.add(product)
    session.commit()
    product = session.scalar(select(Product))
    print(product)
    assert None == False


def test_many_product_for_one_person(session: Session):
    products = FactoryProduct.create_batch(3)
    person = FactoryPerson.build()
    person.products.extend(products)
    session.add(person)
    session.commit()
    person = session.scalar(select(Person))
    print(person)
    assert None == False
