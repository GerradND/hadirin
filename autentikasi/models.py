from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User


class Profile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    ROLE_CHOICES = (
        ('staf', 'Staf'),
        ('sup', 'Supervisor'),
    )
    role = models.CharField(max_length=4, choices=ROLE_CHOICES)

    def __str__(self) -> str:
        return f"{self.user}'s Profile"