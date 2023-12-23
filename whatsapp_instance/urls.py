from django.urls import include, path
from rest_framework.routers import DefaultRouter

from whatsapp_instance.views import ClientMessageViewSet

router = DefaultRouter()
router.register(r"client-messagpipes", ClientMessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
