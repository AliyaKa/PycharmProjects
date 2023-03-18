from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users import models


@admin.register(models.CustomUser)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('firstname', 'lastname', 'password')}),
        (_('Personal info'), {'fields': ('username', 'email')}),
        (_('Permissions'), {
            'fields': ('groups', 'user_permissions', 'is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'firstname', 'is_staff')
    search_fields = ('username', 'firstname', 'email')
