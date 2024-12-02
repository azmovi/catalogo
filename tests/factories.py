from random import randint

import factory

from catalogo.model import Person, Product


class FactoryPerson(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:  # type: ignore
        model = Person

    nick = factory.Faker('user_name')
    name = factory.Faker('name')
    birthday = factory.Faker('date')
    stack = factory.Faker('words', nb=randint(0, 10))
    products = [] 

class FactoryProduct(factory.alchemy.SQLAlchemyModelFactory):
    class Meta: # type: ignore
        model = Product

    nome = factory.Faker('word')
    people = []

