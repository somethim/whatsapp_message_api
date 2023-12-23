from django.urls import include, path
from rest_framework import routers

from .views import ClientsViewSet, CurrentUserViewSet, UserViewSet

app_name = "user_data"

router = routers.SimpleRouter()
router.register(r"staff", UserViewSet, basename="staff")
router.register(r"clients", ClientsViewSet, basename="clients")

urlpatterns = [
    path("", include(router.urls)),
    path("current_user/", CurrentUserViewSet.as_view(), name="current_user"),
]
