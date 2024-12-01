from random import randint

import factory

from catalogo.model import Person, Test


class FactoryPerson(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:  # type: ignore
        model = Person

    nick = factory.Faker('user_name')
    name = factory.Faker('name')
    birthday = factory.Faker('date')
    stack = factory.Faker('words', nb=randint(0, 10))


class FactoryTest(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:  # type: ignore
        model = Test 
        sqlalchemy_session = None

    id = factory.Faker('uuid4')
