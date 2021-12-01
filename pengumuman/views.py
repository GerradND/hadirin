from django.shortcuts import render
from .forms import PengumumanForm
# Dummy Data
thread = {
    'user' : 'Budi Budiman',
    'title' : "Lorem ipsum dolor sit amet conquistador",
    'content' : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
    'replies' : [
        {
            'user' : 'Susan Susanti', 
            'content' : 'Saya Setuju dengan pendapat anda' 
        },
        {
            'user' : 'Rudi Rudiman', 
            'content' : 'Saya tidak etuju' 
        }
    ]
}

threads = [thread, thread]

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