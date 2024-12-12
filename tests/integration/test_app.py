from http import HTTPStatus

from faker import Faker
from fastapi.testclient import TestClient

from catalogo.model import Person
from tests.factories import FactoryPerson


def test_create_full_person(client: TestClient):
    payload = FactoryPerson.build().model_dump()
    del payload['id']

    response = client.post('/people', json=payload)

    data = response.json()
    del data['id']

    assert response.status_code == HTTPStatus.CREATED
    assert data == payload


def test_create_person_without_stack(client: TestClient):
    payload = FactoryPerson.build(stack=None).model_dump()
    del payload['id']

    response = client.post('/people', json=payload)

    data = response.json()
    del data['id']

    assert data == payload
    assert response.status_code == HTTPStatus.CREATED


def test_create_person_fails_without_nick(client: TestClient):
    payload = FactoryPerson.build(nick=None).model_dump()
    del payload['id']

    response = client.post('/people', json=payload)
    data = response.json()

    assert data == {'detail': 'Database integrity error'}
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_person_fails_without_name(client: TestClient):
    payload = FactoryPerson.build(name=None).model_dump()
    del payload['id']

    response = client.post('/people', json=payload)
    data = response.json()

    assert data == {'detail': 'Database integrity error'}
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_person_fails_without_birthday(client: TestClient):
    payload = FactoryPerson.build(birthday=None).model_dump()
    del payload['id']

    response = client.post('/people', json=payload)
    data = response.json()

    assert data == {'detail': 'Database integrity error'}
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_person_fail_nick_exceed_32_characters(client: TestClient):
    payload = FactoryPerson.build(nick='a' * 33).model_dump()
    del payload['id']

    response = client.post('/people', json=payload)
    data = response.json()

    assert data == {'detail': 'Invalid content in field'}
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_person_fail_name_exceed_100_characters(client: TestClient):
    payload = FactoryPerson.build(name='a' * 101).model_dump()
    del payload['id']

    response = client.post('/people', json=payload)
    data = response.json()

    assert data == {'detail': 'Invalid content in field'}
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_person_fail_date_invalid_format(client: TestClient):
    payload = FactoryPerson.build(birthday='28-10-2024').model_dump()
    del payload['id']

    response = client.post('/people', json=payload)
    data = response.json()

    assert data == {'detail': 'Invalid content in field'}
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_get_person(client: TestClient, person: Person):
    nick = person.nick
    person_json = person.model_dump()
    del person_json['id']

    response = client.get(f'/people/{nick}')
    data = response.json()
    del data['id']

    assert data == person_json
    assert response.status_code == HTTPStatus.OK


def test_get_person_not_found(client: TestClient, faker: Faker):
    nick = faker.name()

    response = client.get(f'/people/{nick}')
    data = response.json()

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert data == {'detail': 'Person not found'}


def test_get_person_with_blank_nick(client: TestClient, person: Person):
    nick = ' '

    response = client.get(f'/people/{nick}')
    data = response.json()

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert data == {'detail': 'Person not found'}
