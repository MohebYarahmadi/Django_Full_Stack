import pytest
from apps.users.models import User

# get rid of using `@pytest.mark.django_db` decorator
pytestmark = pytest.mark.django_db

# USE FIXTURE
# ============================
# data_user = {
#     'username': 'test_user',
#     'email': 'test@gmail.com',
#     'first_name': 'Test',
#     'last_name': 'User',
#     'password': 'test_password'
# }

# @pytest.mark.django_db    # don't need it if you have `pytestmark`
# def test_create_user():
#     obj = User.objects.create_user(**data_user)
#     assert obj.username == data_user['username']
#     assert obj.email == data_user['email']
#     assert obj.first_name == data_user['first_name']
#     assert obj.last_name == data_user['last_name']


# def test_create_superuser():
#     obj = User.objects.create_superuser(**data_user)
#     assert obj.username == data_user['username']
#     assert obj.email == data_user['email']
#     assert obj.first_name == data_user['first_name']
#     assert obj.last_name == data_user['last_name']
#     assert obj.is_superuser == True
#     assert obj.is_staff == True
# ==============================

class TestUserModel:
    def test_str_method(self, user_factory):
        user = user_factory.build()
        assert str(user) == user.email  # match whatever __str__ returns

    def test_create_user(self, user_factory):
        kwargs = user_factory.create_user_kwargs()
        obj = User.objects.create_user(**kwargs)

        assert obj.username == kwargs['username']
        assert obj.email == kwargs['email']
        assert obj.check_password(kwargs['password'])

    def test_create_superuser(self, user_factory):
        kwargs = user_factory.create_user_kwargs()
        obj = User.objects.create_superuser(**kwargs)

        assert obj.username == kwargs['username']
        assert obj.email == kwargs['email']
        assert obj.is_superuser is True
        assert obj.is_staff is True
        assert obj.check_password(kwargs['password'])
