from rest_framework import status

from apps.fixtures.users_fixture import user
from apps.fixtures.posts_fixture import post


class TestUserViewSet:
    endpoint = '/api/users/'

    def test_list(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_retrieve(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(
            self.endpoint + str(user.public_id) + '/'
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == user.public_id.hex
        assert response.data["username"] == user.username
        assert response.data["email"] == user.email

    def test_create(self, client, user):
        client.force_authenticate(user=user)
        data = {}
        response = client.post(self.endpoint, data)

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_updata(self, client, user):
        client.force_authenticate(user=user)
        data = {
            "username": "test_user_updated",
        }
        response = client.patch(
            self.endpoint + str(user.public_id) + '/', data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == data["username"]

        # Anonymous
    def test_list_anonymous(self, client, user):
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_retrieve_anonymous(self, client, user):
        response = client.get(
            self.endpoint + str(user.public_id) + '/'
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
