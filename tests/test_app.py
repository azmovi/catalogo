# from http import HTTPStatus
#
# from fastapi.testclient import TestClient
#
# from tests.factories import FactoryPerson
#
# def test_factories(client):
#     user = FactoryPerson()
#     assert user.id == None
#
#
# def test_create_full_person(client: TestClient):
#     payload = FactoryPerson().model_dump()
#     response = client.post('/people', json=payload)
#     data = response.json()
#     print(payload)
#
#     assert data == payload
#     assert response.status_code == HTTPStatus.CREATED
#
#
# def test_create_person_without_stack(client: TestClient):
#     payload = {
#         'nick': 'xpto',
#         'name': 'xpto',
#         'birthday': '2002-07-08',
#     }
#     response = client.post('/people', json=payload)
#     data = response.json()
#     data.pop('id', None)
#
#     assert data == {**payload, 'stack': None}
#     assert response.status_code == HTTPStatus.CREATED
#
#
# def test_create_person_fails_without_required_field(client: TestClient):
#     payload = {
#         'name': 'xpto',
#         'birthday': '2002-07-08',
#         'stack': ['Python'],
#     }
#     response = client.post('/people', json=payload)
#     data = response.json()
#     data.pop('id', None)
#
#     assert data == {'detail': 'Database integrity error'}
#     assert response.status_code == HTTPStatus.BAD_REQUEST
#
#
# def test_create_person_fail_nick_exceed_32_characters(client: TestClient):
#     payload = {
#         'name': 'xpto',
#         'birthday': '2002-07-08',
#         'stack': ['Python'],
#     }
#     response = client.post('/people', json=payload)
#     data = response.json()
#     data.pop('id', None)
#
#     assert data == {'detail': 'Database integrity error'}
#     assert response.status_code == HTTPStatus.BAD_REQUEST
