from rest_framework.routers import DefaultRouter

from whatsapp_instance.views import ClientMessageViewSet

router = DefaultRouter()
router.register(r"client-message", ClientMessageViewSet, basename="client-message")

urlpatterns = router.urls
