from django.shortcuts import render
from .forms import UpdateProfile
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'main/home.html')

def profil(request):
    return render(request, 'main/profil.html')

def profil_edit(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('main:profil'))
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'main/profilEdit.html', args)

def presensi(request):
    return render(request, 'main/presensi.html')

def presensi_edit(request):
    return render(request, 'main/presensiEdit.html')