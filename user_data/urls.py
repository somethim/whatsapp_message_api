from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    ClientsViewSet,
    CompanyViewSet,
    CurrentUserViewSet,
    LogoutView,
    UserViewSet,
)

app_name = "user_data"

router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="staff")
router.register(r"clients", ClientsViewSet, basename="clients")

urlpatterns = [
    path("current-user/", CurrentUserViewSet.as_view(), name="current-user"),
    path("login/", obtain_auth_token, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("company", CompanyViewSet.as_view(), name="company"),
]

urlpatterns += router.urls
