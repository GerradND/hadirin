from django.db import models
from django.contrib.auth.models import User

class RoleDivisi(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    class Meta:
        db_table = 'role_divisi'

    def __str__(self):
        return self.nama
