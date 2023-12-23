from rest_framework import serializers

from whatsapp_instance.models import ClientMessage


class ClientMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientMessage
        fields = (
            "id",
            "client",
            "message",
            "date",
        )
        read_only_fields = ("date", "id")
