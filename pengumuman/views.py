from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import PengumumanForm

# Create your views here.
def pengumuman(request):
    return render(request, 'pengumuman/pengumuman.html')

def pengumuman_saya(request):
    return render(request, 'pengumuman/pengumuman_saya.html')

def buat_pengumuman(request):
    form = PengumumanForm()
    if request.method == 'POST':
        messages.success(request, 'Pengumuman berhasil dibuat!')
        return redirect('pengumuman:pengumuman_saya')
    return render(request, 'pengumuman/buat_pengumuman.html', {'form' : form})

def edit_pengumuman(request):
    form = PengumumanForm()
    if request.method == 'POST':
        messages.success(request, 'Pengumuman berhasil diubah!')
        return redirect('pengumuman:pengumuman_saya')
    return render(request, 'pengumuman/edit_pengumuman.html', {'form' : form})

def hapus_pengumuman(request):
    if request.method == 'POST':
        messages.success(request, 'Pengumuman berhasil dihapus!')
        return redirect('pengumuman:pengumuman_saya')
    return render(request, 'pengumuman/hapus_pengumuman.html')