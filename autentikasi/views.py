from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from autentikasi.forms import UserRegistrationForm
from autentikasi.models import Profile
from role_divisi.models import RoleDivisi
from functools import wraps
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return_url = request.GET.get('next')
            return redirect(return_url or 'main:home')
        else :
            messages.error(request, "Incorrect username or password")
    
    return render(request, 'autentikasi/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('autentikasi:login')

@login_required
def register(request):
    if not request.user.is_superuser:
        messages.error('403 : Unauthorized')
        return redirect('main:home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            divisi_id = form.cleaned_data.get('divisi')
            divisi = RoleDivisi.objects.get(id= divisi_id)
            Profile.objects.create(user=user,role=role, divisi=divisi)
            messages.success(request,'Akun Berhasil Dibuat')
        else:
            print(form.errors)
            messages.error(request, form.errors)

    divisi_list = RoleDivisi.objects.all()
    context = { 'divisi_list' : divisi_list }
    return render(request, 'autentikasi/register.html', context)