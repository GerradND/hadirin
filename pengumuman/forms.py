from django import forms

class PengumumanForm(forms.Form):
    judul = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-isi'}), label='Judul')
    konten = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-isi'}), label='Isi')