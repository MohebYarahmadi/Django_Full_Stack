import pytest
from apps.fixtures.users_fixture import user
from apps.fixtures.posts_fixture import post
from apps.comments.models import Comment

pytestmark = pytest.mark.django_db


# def test_create_comment(user, post):
#     obj = Comment.objects.create(
#         author=user,
#         post=post,
#         body='Test Comment Body'
#     )
#
#     assert obj.author == user
#     assert obj.post == post
#     assert obj.body == 'Test Comment Body'

class TestCommentModel:
    def test_str_method(self, comment_factory):
        comment = comment_factory.build()
        assert str(comment) == comment.author.name

    def test_create_comment(self, comment_factory):
        obj = comment_factory()  # SubFactory + Sequence handle the DB
        assert obj.pk is not None
        assert obj.author.pk is not None
        assert obj.post.pk is not None
        assert obj.body == 'Test Comment Body'
