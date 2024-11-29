# Catalogo

- Api simples para verificar o catalogo de pessoas
- Baseado nesse [repositório](https://github.com/zanfranceschi/rinha-de-backend-2023-q3/)

### Stack
- fastapi
- sqlmodel
- sqlite


### Regras
##### Post
- **apelido**: obrigatório, único, até 32 caracteres.
- **nome**: obrigatório, até 100 caracteres.
- **nascimento**: obrigatório.
- **stack**: opcional, vetor de string de até 32 caracteres cada string.
