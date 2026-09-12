import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register

from .factories import UserFactory


register(UserFactory)   # Usage: `user_factory`

@pytest.fixture
def client():
    return APIClient()
