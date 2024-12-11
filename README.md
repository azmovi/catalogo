# Catalogo

### O que falta fazer
- [ ] Terminar os testes do post
- [ ] Criar as migrations e o entrypoint do alembic para o docker
- [ ] Finalizar os endpoints
- [ ] Finalizar os testes dos novos endpoints
- [ ] Começar os testes bdd

- Api simples para verificar o catalogo de pessoas
- Baseado nesse [repositório](https://github.com/zanfranceschi/rinha-de-backend-2023-q3/)

### Stack
- fastapi
- sqlmodel
- postgres
- docker


### Regras
##### Post
- **apelido**: obrigatório, único, até 32 caracteres.
- **nome**: obrigatório, até 100 caracteres.
- **nascimento**: obrigatório.
- **stack**: opcional, vetor de string de até 32 caracteres cada string.
