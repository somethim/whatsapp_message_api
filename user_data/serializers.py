from rest_framework import serializers

from user_data.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "phone",
            "email",
            "is_superuser",
        )
        read_only_fields = ("id", "is_superuser")
