from rest_framework import status

from apps.fixtures.users_fixture import user
from apps.fixtures.posts_fixture import post
from apps.fixtures.comments_fixture import comment


class TestCommentViewSet:
    # The comment resouce is nested under the post resouce
    endpoint = '/api/posts/'

    def test_list(self, client, user, post, comment):
        client.force_authenticate(user=user)
        response = client.get(
            self.endpoint + str(post.public_id) + '/comments/'
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_retrieve(self, client, user, post, comment):
        client.force_authenticate(user=user)
        response = client.get(
            self.endpoint
            + str(post.public_id) + '/comments/'
            + str(comment.public_id) + '/'
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == comment.public_id.hex
        assert response.data['body'] == comment.body
        assert response.data['author']['id'] == comment.author.public_id.hex

    def test_create(self, client, user, post):
        client.force_authenticate(user=user)
        data = {
            'body': 'Test Comment Body',
            'author': user.public_id.hex,
            'post': post.public_id.hex
        }
        response = client.post(
            self.endpoint + str(post.public_id) + '/comments/',
            data
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['body'] == data['body']
        assert response.data['author']['id'] == user.public_id.hex

    def test_update(self, client, user, post, comment):
        client.force_authenticate(user=user)
        data = {
            'body': 'Test Comment Body Updated',
            'author': user.public_id.hex,
            'post': post.public_id.hex
        }
        response = client.put(
            self.endpoint
            + str(post.public_id.hex) + '/comments/'
            + str(comment.public_id.hex) + '/',
            data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data['body'] == data['body']

    def test_delete(self, client, user, post, comment):
        client.force_authenticate(user=user)
        response = client.delete(
            self.endpoint
            + str(post.public_id.hex) + '/comments/'
            + str(comment.public_id.hex) + '/'
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

    # Anonymous
    def test_list_anonymous(self, client, post, comment):
        response = client.get(
            self.endpoint + str(post.public_id) + '/comments/'
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_retrieve_anonymous(self, client, post, comment):
        response = client.get(
            self.endpoint
            + str(post.public_id) + '/comments/'
            + str(comment.public_id) + '/'
        )

        assert response.status_code == status.HTTP_200_OK

    def test_create_anonymous(self, client, post):
        data = {}

        response = client.post(
            self.endpoint
            + str(post.public_id) + '/comments/',
            data
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_updata_anonymous(self, client, post, comment):
        data = {}

        response = client.put(
            self.endpoint
            + str(post.public_id) + '/comments/'
            + str(comment.public_id) + '/',
            data
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_anonymous(self, client, post, comment):
        response = client.delete(
            self.endpoint
            + str(post.public_id) + '/comments/'
            + str(comment.public_id) + '/'
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
