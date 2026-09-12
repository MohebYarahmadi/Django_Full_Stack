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
