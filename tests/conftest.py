import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register

from .factories import (
    UserFactory, PostFactory, CommentFactory
)


register(UserFactory)   # Usage: `user_factory`
register(PostFactory)
register(CommentFactory)

@pytest.fixture
def client():
    return APIClient()
