from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import Serializer

from user_data.models import Client
from whatsapp_instance.serializers import MessageSerializer
from whatsapp_message_api.minxin import PermissionPolicyMixin

# TODO: Make the message sending process asynchronous
# TODO: Make message be sent a day before the meeting date
# TODO: Make the message be sent with a specific template


class ClientMessageViewSet(viewsets.ModelViewSet, PermissionPolicyMixin):
    serializer_class = MessageSerializer
    permission_classes_per_method = {
        "retrieve": [IsAdminUser],
        "list": [IsAdminUser],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_queryset(self) -> QuerySet:
        return Client.objects.filter(
            company=self.request.user.company,
        ).order_by("name")

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(company=self.request.user.company)
