import pytest
from rest_framework import status

from apps.fixtures import user


class TestAuthenticaionViewSet:
    endpoint = '/api/auth/'
