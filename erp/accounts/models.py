#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib import admin


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_account"

    # bio = models.CharField(max_length=256, blank=True)

