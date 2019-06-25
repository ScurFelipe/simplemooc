from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'email']
    search_fields = ['name']


admin.site.register(User, UserAdmin)
