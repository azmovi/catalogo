from random import randint
from datetime import datetime

import factory

from catalogo.model import Person
from catalogo.database import get_session


class PersonFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:  # type: ignore
        model = Person
        sqlalchemy_session = next(get_session())

    nick = factory.Faker('user_name')
    name = factory.Faker('name')
    birthday = '2010-10-10'
    stack = factory.Faker('words', nb=randint(0, 10))

a = PersonFactory.build()
print(a)
a = PersonFactory.create()
print(a)

