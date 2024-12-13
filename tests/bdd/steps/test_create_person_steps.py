from http import HTTPStatus

from pytest_bdd import given, scenarios, then, when

from catalogo.model import Person

scenarios('../features/people_api.feature')


@given('que o banco de dados está vazio')
def empty_database(session) -> None:
    session.query(Person).delete()
    session.commit()


@when(
    'o usuario envia uma requisição POST com os dados:',
    target_fixture="response"
)
def xpto(datatable, client) -> dict[str, str]:
    user_data = datatable[1]
    data = {
        'nick': user_data[0],
        'name': user_data[1],
        'birthday': user_data[2],
        'stack': user_data[3].split(', '),
    }

    response = client.post('/people', json=data)
    return response


@then('eu recebo uma resposta com status criado')
def check_success_status(response) -> None:
    assert response.status_code == HTTPStatus.CREATED


@then('os dados da pessoa criada são retornados')
def check_person_created(response) -> None:
    data = response.json()

    assert data['nick'] == 'Luizito'
    assert data['name'] == 'Lui Lui'
    assert data['birthday'] == '1990-01-01'
    assert data['stack'] == ['Python', 'Node']
