import pytest
from apps.posts.models import Post
from apps.fixtures.users_fixture import user

pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_str_method(self, post_factory):
        post = post_factory.build()
        assert str(post) == post.author.name

    def test_create_post(self, post_factory):
        kwargs = post_factory.create_post_kwargs()
        obj  = Post.objects.create(**kwargs)

        assert obj.author == kwargs['author']
        assert obj.body == kwargs['body']
        assert obj.edited == kwargs['edited']
