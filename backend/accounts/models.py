from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


# User = get_user_model()

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

# ! Bad idea
# class MyUser(User):
#     pass


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
