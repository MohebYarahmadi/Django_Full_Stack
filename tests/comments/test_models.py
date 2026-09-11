import pytest
from apps.fixtures.users_fixture import user
from apps.fixtures.posts_fixture import post
from apps.comments.models import Comment

pytestmark = pytest.mark.django_db


def test_create_comment(user, post):
    obj = Comment.objects.create(
        author=user,
        post=post,
        body='Test Comment Body'
    )

    assert obj.author == user
    assert obj.post == post
    assert obj.body == 'Test Comment Body'
