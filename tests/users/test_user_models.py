import pytest
from apps.users.models import User
from apps.fixtures.users_fixture import user

# get rid of using `@pytest.mark.django_db` decorator
pytestmark = pytest.mark.django_db


data_user = {
    'username': 'test_use',
    'email': 'test@gmail.com',
    'first_name': 'Test',
    'last_name': 'User',
    'password': 'test_password'
}

# @pytest.mark.django_db    # don't need it if you have `pytestmark`
def test_create_user():
    user = User.objects.create_user(**data_user)
    assert user.username == data_user['username']
    assert user.email == data_user['email']
    assert user.first_name == data_user['first_name']
    assert user.last_name == data_user['last_name']


def test_create_superuser():
    user = User.objects.create_superuser(**data_user)
    assert user.username == data_user['username']
    assert user.email == data_user['email']
    assert user.first_name == data_user['first_name']
    assert user.last_name == data_user['last_name']
    assert user.is_superuser == True
    assert user.is_staff == True
