from django.contrib.auth.models import User
from django import forms
from django.forms import fields
from .models import Presensi
import datetime

class IsiPresensi(forms.ModelForm):
    masuk = forms.DateTimeField(required=True)
    class  Meta:
        model = Presensi
        fields = ('masuk',)
    def save(self, user:User):
        filterPresensi=Presensi.objects.filter(masuk__date=datetime.date.today())
        print(filterPresensi)
        print(filterPresensi)
        if(len(filterPresensi)==0):
            print('masuk')
            # Presensi.objects.create(masuk = datetime.datetime.now, user_id=user.id)
            presensi  = Presensi(masuk = datetime.datetime.now())
            presensi.user_id = user.id
            presensi.save()
        else:
            print('keluar')
            presensi = filterPresensi.first()
            presensi.keluar = datetime.datetime.now()
            presensi.save()

class UpdateProfile(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def save(self, user:User):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
            
        return user