from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_verified', 'bio', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_verified', 'bio', 'profile_picture')}),
    )
    list_display = ['username', 'email', 'is_verified', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
