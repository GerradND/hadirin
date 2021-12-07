from django import forms
from .models import Pengumuman

class PengumumanForm(forms.ModelForm):
    class Meta:
        model = Pengumuman
        fields = ["judul", "isi"]
    
    error_messages = {
        'required' : 'Informasi Wajib Diisi'
    }
    
    input_attrs_judul = {
        'type' : 'text',
        'placeholder' : 'Judul Pengumuman',
        'class' : 'form-control',
        'autocomplete' : 'off',
        'required' : True
    }
    
    input_attrs_isi = {
        'type' : 'text',
        'placeholder' : 'Isi Pengumuman',
        'class' : 'form-control',
        'autocomplete' : 'off',
        'required' : True
    }
    
    judul = forms.CharField(label='Judul', max_length=150, widget=forms.TextInput(attrs=input_attrs_judul))
    isi = forms.CharField(label='Isi', widget=forms.Textarea(attrs=input_attrs_isi))