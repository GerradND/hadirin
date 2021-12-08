from django.db import models


class Izin(models.Model):
    id = models.AutoField(primary_key=True)
    # staf = models.ForeignKey(User, on_delete=models.CASCADE)
    staf = models.CharField(max_length=20)
    tanggal = models.DateField()
    keterangan = models.TextField()
    status = models.CharField(max_length=10, default="Pending")

    def __str__(self):
        return f'{self.id}. {self.staf} {self.tanggal}'
