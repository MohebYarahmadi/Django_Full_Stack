from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.abstracts.serializers import AbstractSerializer
from apps.posts.models import Post
from apps.users.models import User


class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')

    class Meta:
        model = Post
        # List all the fields that can be included in a request or a response
        fields = [
            'id',
            'author',
            'body',
            'edited',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['edited']

    def validate_author(self, value):
        if self.context['request'].user != value:
            reaise ValidationError("You can't create a post for another user.")

        return value
