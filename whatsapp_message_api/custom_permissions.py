from typing import Optional

from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class IsSuperUser(BasePermission):
    def has_permission(self, request: Request, view: Optional[APIView]) -> bool:
        return bool(
            request.user
            and not isinstance(request.user, AnonymousUser)
            and request.user.is_superuser is True
        )
