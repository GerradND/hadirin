from .models import Izin
from .forms import IzinForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


@login_required
def index(request):
    if request.user.profile.role == "staf":
        return render(request, 'perizinan/index.html')
    elif request.user.profile.role == "sup":
        daftar_izin = Izin.objects.filter(
            staf__profile__divisi=request.user.profile.divisi).order_by('status')
        return render(request, 'perizinan/validasi_izin.html', {'daftar_izin': daftar_izin})
    else:
        return redirect('main:home')


@login_required
def add_izin(request):
    if request.user.profile.role == "staf":
        form = IzinForm(request.POST)
        if request.method == 'POST':
            form = IzinForm(request.POST)
            if form.is_valid():
                izin = form.save(commit=False)
                izin.staf = request.user
                izin.save()
                messages.success(
                    request, 'Izin berhasil diajukan ke supervisor')
                return redirect('perizinan:index')
            else:
                messages.error(request, form.errors)
        return render(request, 'perizinan/add_izin.html', {'form': form})
    else:
        return redirect('main:home')


@login_required
def detail_izin(request, id):
    if request.user.profile.role == "sup":
        izin = get_object_or_404(Izin, pk=id)
        if request.method == 'POST':
            status = request.POST['status']
            izin.status = status
            izin.save()
            return redirect('perizinan:index')
        return render(request, 'perizinan/detail_izin.html', {'izin': izin})
    else:
        return redirect('main:home')
