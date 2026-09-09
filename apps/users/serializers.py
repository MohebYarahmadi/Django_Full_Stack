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
