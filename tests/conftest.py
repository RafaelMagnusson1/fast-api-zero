"""Arquivo criado para utilizar fixtures:
uma forma de centralizar recursos comuns de teste"""

from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.models import table_registry

# Fixture de testes da API


@pytest.fixture
def client():
    return TestClient(app)


# Fixture do DB:


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


# Vamos utilizar SQLite como banco em memória
# para os testes
# Fixture está apagando os dados a cada teste
# , para isolá-los


# Para fazer a validação dos campos do
# objeto durante os testes,
# Criamos um evento:


@contextmanager
def _mock_db_time(*, model, time=datetime(2024, 1, 1)):
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = time

    event.listen(model, 'before_insert', fake_time_hook)

    yield time

    event.remove(model, 'before_insert', fake_time_hook)


# Transformando o evento numa fixture


@pytest.fixture
def mock_db_time():
    return _mock_db_time
