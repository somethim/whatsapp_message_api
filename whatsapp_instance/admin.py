from django.contrib import admin

from .models import Clients


# Register your models here.
class ClientsAdmin(admin.ModelAdmin):
    class Meta:
        model = Clients


admin.site.register(Clients, ClientsAdmin)
