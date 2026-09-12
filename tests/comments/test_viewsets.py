from rest_framework import status

from apps.fixtures.users_fixture import user
from apps.fixtures.posts_fixture import post
from apps.fixtures.comments_fixture import comment


class TestCommentViewSet:
    # The comment resouce is nested under the post resouce
    endpoint = '/api/posts/'

    def test_list(self, client, user, post, comment):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(post.public_id) + '/comments/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_retrieve(self, client, user, post, comment):
        client.force_authenticate(user=user)
        response = client.get(
            self.endpoint + str(post.public_id)
            + '/comments/' + str(comment.public_id) + '/'
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == comment.public_id.hex
        assert response.data['body'] == comment.body
        assert response.data['author']['id'] == comment.author.public_id.hex
