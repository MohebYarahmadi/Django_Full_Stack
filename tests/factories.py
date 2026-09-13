import factory

from apps.users.models import User
from apps.posts.models import Post
from apps.comments.models import Comment


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'test_user_{n}')
    email = factory.Sequence(lambda n: f'test_mail_{n}@example.com')
    password = 'test_password'
    first_name = 'Test'
    last_name = 'User'

    @classmethod
    def create_user_kwargs(cls, **overrides):
        user = cls.build(**overrides)
        return {
            'username': user.username,
            'email': user.email,
            'password': user.password,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }

    # If you'd rather get a dict back (useful if you want to filter keys generically)
    # use factory.attributes():
    # @classmethod
    # def create_user_kwargs(cls, **overrides):
    #     data = cls.attributes(**overrides)  # returns dict
    #     return {
    #         'username': data['username'],
    #         'email': data['email'],
    #         'password': data['password'],
    #         'first_name': data['first_name'],
    #         'last_name': data['last_name'],
    #     }


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    body = 'Test Post Body'
    edited = False

    @classmethod
    def create_post_kwargs(cls, **overrides):
        post = cls.create(**overrides)
        return {
            'author': post.author,
            'body': post.body,
            'edited': post.edited
        }


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment
        django_get_or_create = ('post', 'author')

    author = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    body = 'Test Comment Body'

    @classmethod
    def create_comment_kwargs(cls, **overrides):
        # Build only — don't hit the DB here
        comment = cls.build(**overrides)
        return {
            'author': comment.author,
            'post': comment.post,
            'body': comment.body,
        }
