from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Izin
import datetime


class IzinForm(forms.ModelForm):
    class Meta:
        model = Izin
        fields = ['tanggal', 'keterangan']

        tanggal_attr = {
            'type': 'date',
            'min': datetime.date.today() + datetime.timedelta(days=3),
            'placeholder': 'Tanggal',
            'class': 'form-input',
        }

        keterangan_attr = {
            'type': 'text',
            'placeholder': 'Tambah keterangan . . .',
            'class': 'form-input',
        }

        widgets = {
            'tanggal': forms.DateInput(attrs=tanggal_attr),
            'keterangan': forms.Textarea(attrs=keterangan_attr)
        }
