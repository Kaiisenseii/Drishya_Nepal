from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
from .models import DrishyaNepalUser

class DrishyaNepalUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password','first_name', 'last_name','email', 'phone','address', 'profile_pic', 'is_customer', 'is_photographer')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )

admin.site.register(DrishyaNepalUser, DrishyaNepalUserAdmin)