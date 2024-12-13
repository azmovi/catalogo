# language: pt

Funcionalidade: Criar uma nova pessoa
    Testes para registrar novas pessoas no sistema

    Cenário: Criação com sucesso
        Dado que o banco de dados está vazio
        Quando o usuario envia uma requisição POST com os dados:
            | nick    | name    | birthday   | stack        | 
            | Luizito | Lui Lui | 1990-01-01 | Python, Node |
        Então eu recebo uma resposta com status criado
        E os dados da pessoa criada são retornados
