from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.abstracts.serializers import AbstractSerializer
from apps.users.serializers import UserSerializer
from apps.users.models import User
from apps.posts.models import Post


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
            raise ValidationError("You can't create a post for another user.")

        return value

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data
        return rep

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True

        instance = super().update(instance, validated_data)

        return instance
