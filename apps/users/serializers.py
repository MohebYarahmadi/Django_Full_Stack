from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

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
