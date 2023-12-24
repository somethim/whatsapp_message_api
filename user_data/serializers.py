from rest_framework import serializers

from user_data.models import Client, User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "phone_number",
            "email",
        )
        read_only_fields = ("id",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "phone_number",
            "email",
            "is_superuser",
        )
        read_only_fields = ("id", "is_superuser")


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "name",
            "phone_number",
            "email",
            "company",
            "message",
            "next_meeting_date",
        )
        read_only_fields = ("id", "company")
