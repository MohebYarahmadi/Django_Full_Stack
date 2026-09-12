import pytest
from apps.posts.models import Post
from apps.fixtures import user

pytestmark = pytest.mark.django_db


def test_create_post(user):
    post = Post.objects.create(author=user, body='Test Post Body')

    assert post.body == 'Test Post Body'
    assert post.author == user
