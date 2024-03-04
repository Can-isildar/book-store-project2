from django.contrib import admin
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm
    model = CustomUser
    list_display = ["email", "username", "first_name", "last_name", "password"]


admin.site.register(CustomUser, CustomUserAdmin)
