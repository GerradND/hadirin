from django.db import models


class RoleDivisi(models.Model):
    name = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, RoleDivisi):
            return NotImplemented
        return self.name == other.name
