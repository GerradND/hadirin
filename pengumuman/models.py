from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pengumuman(models.Model):
    judul = models.CharField(max_length = 150)
    isi = models.TextField()
    user =  models.ForeignKey(User, on_delete = models.CASCADE)
    tanggal_post = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)