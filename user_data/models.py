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
        return self.create_staff(
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

    def __str__(self) -> str:
        return f"{self.name}"


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, default=None, null=True, blank=True)
    phone_number = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)

    company = models.ForeignKey("user_data.Company", on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone"]

    def __str__(self) -> str:
        return f"{self.name} - {self.email} | {self.phone_number}"


class Client(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    next_meeting_date = models.DateTimeField(default=None, null=True, blank=True)

    message = models.TextField(default=None, null=True, blank=True)
    company = models.ForeignKey("user_data.Company", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} - {self.phone_number} | {self.email}"
