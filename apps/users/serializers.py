from rest_framework import serializers

from apps.abstracts.serializers import AbstractSerializer
from apps.users.models import User


class UserSerializer(AbstractSerializer):

    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "created_at",
            "updated_at",
        ]
        # List of all the fields that can only be read by the user
        read_only_field = ["is_active"]

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            if not representation['avatar']:
                representation['avatar'] = settings.DEFAULT_AUTO_FIELD
                return representation
            if settings.DEBUG == True:
                request = self.context.get('request')
                representation['avatar'] = request.build_absolute_uri(
                    representation['avatar']
                )
                return representation
