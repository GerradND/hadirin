from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.

def login_view(request):
    return render(request, 'autentikasi/login.html')

def logout_view(request):
    logout(request)
    return redirect('autentikasi:login')


def register(request):
    return render(request, 'autentikasi/register.html')