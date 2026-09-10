from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.abstracts.serializers import AbstractSerializer
from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.comments.models import Comment
from apps.posts.models import Post


class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='public_id')

    class Meta:
        model = Comment
        # List of all the fields that can be included in a request or a response
        fields = [
        'id',
        'post',
        'author',
        'body',
        'edited',
        'created_at',
        'updated_at'
        ]
        read_only_fields = ['edited']

    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)

        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data

        return rep
