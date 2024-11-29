from fastapi.testclient import TestClient


def test_create_person(client: TestClient):
    data = {
        'nick': 'xpto',
        'name': 'xpto',
        'birthday': '2002-07-08',
        'stack': ['Python']
    }
    response = client.post('/person', json=data)

    assert response
