from typing import Optional

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_superuser(
        self,
        phone: str,
        email: str,
        is_superuser: bool = True,
        is_staff: bool = True,
        is_active: bool = True,
        name: Optional[str] = None,
        password: Optional[str] = None,
    ) -> "User":
        return self.create_user(
            name=name,
            phone=phone,
            email=email,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active,
            password=password,
        )

    def create_staff(
        self,
        phone: str,
        email: str,
        is_superuser: bool = False,
        is_staff: bool = True,
        is_active: bool = True,
        name: Optional[str] = None,
        password: Optional[str] = None,
    ) -> "User":
        return self.create_user(
            name=name,
            phone=phone,
            email=email,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active,
            password=password,
        )

    def create_user(
        self,
        phone: str,
        email: str,
        is_superuser: bool = False,
        is_staff: bool = False,
        is_active: bool = True,
        name: Optional[str] = None,
        password: Optional[str] = None,
    ) -> "User":
        user: User = self.model(  # type: ignore
            name=name,
            phone=phone,
            email=email,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Company(models.Model):
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}"


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, default=None, null=True, blank=True)
    phone = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone"]

    def __str__(self) -> str:
        return f"{self.name} - {self.email} | {self.phone}"
