from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Izin(models.Model):
    id = models.AutoField(primary_key=True)
    staf = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal = models.DateField()
    keterangan = models.TextField()
    IZIN_STATUS_CHOICES = [
        ("PD", "Pending"),
        ("ST", "Disetujui"),
        ("TL", "Ditolak")
    ]
    status = models.CharField(
        max_length=10, choices=IZIN_STATUS_CHOICES, default="PD")

    def __str__(self):
        return f'{self.id}. {self.staf} {self.tanggal}'
