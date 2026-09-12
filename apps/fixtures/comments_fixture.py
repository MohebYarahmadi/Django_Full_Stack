import pytest

from apps.fixtures.posts_fixture import post

from apps.comments.models import Comment

@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(author=user, post=post, body='Test Comment Body')
