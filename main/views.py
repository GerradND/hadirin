from datetime import datetime
from django.shortcuts import render
from .forms import IsiPresensi
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, 'main/home.html')

def profil(request):
    return render(request, 'main/profil.html')

def profil_edit(request):
    return render(request, 'main/profilEdit.html')

def presensi(request):
    return render(request, 'main/presensi.html')

def presensi_edit(request):
    args = {}

    if request.method == 'POST':
        form = IsiPresensi(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('main:presensi'))
    else:
        form = IsiPresensi(initial={'masuk': datetime.now(), 'user': request.user})

    args['form'] = form
    return render(request, 'main/presensiEdit.html', args)
