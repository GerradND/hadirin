from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    ROLE_CHOICES = (
        ('staf', 'Staf'),
        ('sup', 'Supervisor'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    divisi = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']