from django.contrib import admin

from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "external_id", "name")


admin.site.register(Users, UsersAdmin)
