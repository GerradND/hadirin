from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'autentikasi/login.html')

def register(request):
    return render(request, 'autentikasi/register.html')