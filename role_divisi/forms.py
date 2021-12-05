from django.forms import ModelForm
from .models import RoleDivisi


class RoleDivisiForm(ModelForm):
    class Meta:
        model = RoleDivisi
        fields = '__all__'
