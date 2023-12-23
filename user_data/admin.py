from django.contrib import admin

from .models import Client, User


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User


class ClientsAdmin(admin.ModelAdmin):
    class Meta:
        model = Client


admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientsAdmin)
