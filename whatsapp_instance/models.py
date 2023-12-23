from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    company = models.ForeignKey("user_data.Company", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} - {self.phone} | {self.email}"
