from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')

def profil(request):
    return render(request, 'main/profil.html')

def profil_edit(request):
    return render(request, 'main/profilEdit.html')

def presensi(request):
    return render(request, 'main/presensi.html')

def presensi_edit(request):
    return render(request, 'main/presensiEdit.html')