from typing import Dict, List, Type

from django.http import HttpRequest
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView


class PermissionPolicyMixin(APIView):
    permission_classes_per_method: Dict[str, List[Type[BasePermission]]]

    def check_permissions(self, request: HttpRequest) -> None:
        try:
            handler = getattr(self, request.method.lower()) if request.method else None
        except AttributeError:
            handler = None

        if (
            handler
            and self.permission_classes_per_method
            and self.permission_classes_per_method.get(handler.__name__)
        ):
            self.permission_classes = self.permission_classes_per_method.get(
                handler.__name__
            )

        super().check_permissions(request)
