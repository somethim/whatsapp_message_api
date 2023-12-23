from typing import Any

from django.http import HttpRequest
from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    """
    Global permission check for superuser.
    """

    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        return bool(request.user and request.user.is_superuser)
