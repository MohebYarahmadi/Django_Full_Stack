import pytest
from apps.fixtures.users_fixture import user
from apps.fixtures.posts_fixture import post
from apps.comments.models import Comment

pytestmark = pytest.mark.django_db
