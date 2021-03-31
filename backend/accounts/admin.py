from django.contrib import admin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = [
        'date_joined',
        'last_login',
        'password',
        'is_active',
    ]
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
