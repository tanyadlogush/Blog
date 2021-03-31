from django import forms

# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# User = get_user_model()

# class UserCreationForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=100)
#     re_password = forms.CharField(max_length=100)

# class UserCreationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["username", "password"]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields