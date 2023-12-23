from django.db import models


class ClientMessage(models.Model):
    client = models.ForeignKey("user_data.Client", on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.client.name} - {self.message[:20]} | {self.date}"
