from django.db import models
import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# -- coding: UTF-8
# Create your models here.

class Presensi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    masuk = models.DateTimeField('Masuk', blank=True)
    keluar = models.DateTimeField('Keluar', blank=True, null=True)
    #def __str__(self):
    #    return (f'{str(self.user[0])} {str(self.masuk)} {str(self.keluar)}')
    def __str__(self):
        #return self.user.get_username()
        return(f"{self.user.get_username()}, id {self.user.id},Masuk di {self.masuk}, Keluar di {self.keluar}")