from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
            'last_name', 'email', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_filed = ['is_active']
