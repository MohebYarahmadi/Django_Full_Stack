import pytest

from apps.fixtures.users_fixture import user
from apps.posts.models import Post


@pytest.fixture
def post(db, user) -> Post:
    return Post.objects.create(author=user, body='Test Post Body')
