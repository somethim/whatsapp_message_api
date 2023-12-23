from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Clients
from .serializers import ClientsSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    serializer_class = ClientsSerializer
    permission_classes_per_method = {
        "retrieve": [IsAdminUser],
        "list": [IsAdminUser],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_queryset(self) -> QuerySet:
        return Clients.objects.filter(company=self.request.user.company).order_by(
            "name"
        )

    def perform_create(self, serializer: ClientsSerializer) -> None:
        serializer.save(company=self.request.user.company)
