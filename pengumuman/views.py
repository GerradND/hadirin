from django.shortcuts import render
from .forms import PengumumanForm

# Create your views here.
def pengumuman(request):

    return render(request, 'pengumuman/pengumuman.html')

def pengumuman_saya(request):
    return render(request, 'pengumuman/pengumuman_saya.html')

def buat_pengumuman(request):
    form = PengumumanForm()
    return render(request, 'pengumuman/buat_pengumuman.html', {'form' : form})

def edit_pengumuman(request):
    form = PengumumanForm()
    return render(request, 'pengumuman/edit_pengumuman.html', {'form' : form})

def hapus_pengumuman(request):
    return render(request, 'pengumuman/hapus_pengumuman.html')