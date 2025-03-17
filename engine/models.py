from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('manager', 'Manager'),
        ('user', 'User'),
        ('public', 'Public'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='public')


class InstalledModule(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    base_url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
