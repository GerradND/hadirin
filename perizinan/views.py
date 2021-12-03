from .models import Izin
from .forms import IzinForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
import datetime


def index(request):
    return render(request, 'perizinan/index.html')


def add_izin(request):
    form = IzinForm(request.POST)

    if request.method == 'POST':
        form = IzinForm(request.POST)
        if form.is_valid():
            print(request.POST)
            izin = form.save(commit=False)
            izin.staf = request.user
            izin.save()
        return redirect('perizinan:index')
    return render(request, 'perizinan/add_izin.html', {'form': form})


def validasi_izin(request):
    daftar_izin = Izin.objects.all()
    return render(request, 'perizinan/validasi_izin.html', {'daftar_izin': daftar_izin})


def detail_izin(request, id):
    izin = get_object_or_404(Izin, pk=id)
    if request.method == 'POST':
        status = request.POST['status']
        izin.status = status
        izin.save()
        return redirect('perizinan:validasi_izin')
    return render(request, 'perizinan/detail_izin.html', {'izin': izin})
