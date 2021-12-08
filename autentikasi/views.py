from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from autentikasi.forms import UserRegistrationForm
from autentikasi.models import Profile

def login_view(request):
    return render(request, 'autentikasi/login.html')

def logout_view(request):
    logout(request)
    return redirect('autentikasi:login')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            Profile.objects.create(user=user,role=role)
            return redirect('autentikasi:login')
        else:
            messages.error(request, form.errors)

    return render(request, 'autentikasi/register.html')