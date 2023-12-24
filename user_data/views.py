from django.db.models import QuerySet
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from user_data.models import Client, User
from user_data.serializers import ClientsSerializer, CompanySerializer, UserSerializer
from whatsapp_message_api.custom_permissions import IsSuperUser
from whatsapp_message_api.minxin import PermissionPolicyMixin


class CompanyViewSet(generics.RetrieveUpdateAPIView, PermissionPolicyMixin):
    serializer_class = CompanySerializer
    permission_classes_per_method = {
        "retrieve": [IsAdminUser],
        "list": [IsAdminUser],
        "create": [IsSuperUser],
        "update": [IsSuperUser],
        "partial_update": [IsSuperUser],
        "destroy": [IsSuperUser],
    }

    def get_queryset(self) -> QuerySet:
        return self.request.user.company


class CurrentUserViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self) -> User:
        return self.request.user


class UserViewSet(viewsets.ModelViewSet, PermissionPolicyMixin):
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


class ClientsViewSet(viewsets.ModelViewSet, PermissionPolicyMixin):
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
        return Client.objects.filter(company=self.request.user.company).order_by("name")

    def perform_create(self, serializer: ClientsSerializer) -> None:
        serializer.save(company=self.request.user.company)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self: Request) -> Response:
        self.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
