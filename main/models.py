from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Presensi(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE),
    masuk = models.DateTimeField('Masuk', blank=True)
    keluar = models.DateTimeField('Keluar', blank=True, null=True)
    def __str__(self):
        return (f'{str(self.user[0])} {str(self.masuk)} {str(self.keluar)}')