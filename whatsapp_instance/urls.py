from django.urls import include, path
from rest_framework import routers

from .views import ClientsViewSet

app_name = "whatsapp_instance"

router = routers.SimpleRouter()
router.register(r"clients", ClientsViewSet, basename="clients")

urlpatterns = [
    path("", include(router.urls)),
]
