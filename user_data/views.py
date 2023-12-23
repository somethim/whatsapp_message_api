from django.db.models import QuerySet
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import Serializer

from user_data.models import User
from user_data.serializers import UserSerializer
from whatsapp_message_api.custom_permissions import IsSuperUser


class CurrentUserViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self) -> QuerySet:
        return self.request.user


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes_per_method = {
        "retrieve": [IsAdminUser],
        "list": [IsAdminUser],
        "create": [IsSuperUser],
        "update": [IsSuperUser],
        "partial_update": [IsSuperUser],
        "destroy": [IsSuperUser],
    }

    def get_queryset(self) -> QuerySet:
        return User.objects.filter(company=self.request.user.company).order_by("name")

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(company=self.request.user.company, is_staff=True)
