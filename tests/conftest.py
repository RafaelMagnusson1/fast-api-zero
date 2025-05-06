"""Arquivo criado para utilizar fixtures:
uma forma de centralizar recursos comuns de teste"""

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)
