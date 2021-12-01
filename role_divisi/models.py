from django.db import models


class RoleDivisi(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

    def __eq__(self, other):
        if not isinstance(other, RoleDivisi):
            return NotImplemented
        return self.nama == other.nama

    class Meta:
        verbose_name = "role_divisi"
        verbose_name_plural = "role_divisi"
