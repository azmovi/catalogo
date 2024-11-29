"""API"""
from fastapi import FastAPI

app = FastAPI()


@app.post('/pessoas', response_model=str)
def create(pessoa: Pessoa):

