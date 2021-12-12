from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
from role_divisi.models import RoleDivisi


class Profile(models.Model):
    ROLE_CHOICES = (
        ('staf', 'Staf'),
        ('sup', 'Supervisor'),
    )
    user = OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=4, choices=ROLE_CHOICES)
    divisi = models.ForeignKey(RoleDivisi, on_delete=models.SET_NULL, null=True, related_name='divisi')

    def __str__(self) -> str:
        return f"{self.user}'s Profile"