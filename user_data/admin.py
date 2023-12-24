from django.contrib import admin

from .models import Client, Company, User


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User


class CompanyAdmin(admin.ModelAdmin):
    class Meta:
        model = Company


class ClientsAdmin(admin.ModelAdmin):
    class Meta:
        model = Client


admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Client, ClientsAdmin)
