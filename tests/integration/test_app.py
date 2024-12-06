from http import HTTPStatus

from fastapi.testclient import TestClient

from tests.factories import FactoryPerson
from catalogo.model import Person


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
    payload = FactoryPerson.build(nick='a'*50).model_dump()
    del payload['id']
    print(payload)

    response = client.post('/people', json=payload)
    data = response.json()
    data.pop('id', None)

    assert data == {'detail': 'Database integrity error'}
    assert response.status_code == HTTPStatus.BAD_REQUEST
