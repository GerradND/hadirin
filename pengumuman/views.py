from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from .forms import PengumumanForm
from .models import Pengumuman


# Create your views here.
context = {}

@login_required
def pengumuman(request):
    user = User.objects.get(id=request.user.id) #!!!
    pengumuman = Pengumuman.objects.order_by("-tanggal_post")
    context["pengumuman"] = pengumuman
    context["user"] = user
    return render(request, 'pengumuman/pengumuman.html', context)

@login_required
def pengumuman_saya(request):
    user = User.objects.get(id = request.user.id)
    pengumuman = Pengumuman.objects.filter(user = user).order_by("-tanggal_post")
    context["pengumuman"] = pengumuman
    context["user"] = request.user.username
    return render(request, 'pengumuman/pengumuman_saya.html', context)

@login_required
def buat_pengumuman(request):
    context["user"] = request.user.username
    context["form"] = PengumumanForm()
    if request.method == 'POST':
        user = User.objects.get(id = request.user.id)
        form = PengumumanForm(request.POST or None)
        if request.POST and form.is_valid():
            judul = form.cleaned_data['judul']
            isi = form.cleaned_data['isi']
            pengumuman = Pengumuman.objects.create(judul = judul, isi = isi, user=user)
            messages.success(request, 'Pengumuman berhasil dibuat!')
            return redirect('pengumuman:pengumuman_saya')
        else:
            messages.error(request, 'Form tidak berhasil dibuat!')
            return redirect("pengumuman:buat_pengumuman")
    return render(request, 'pengumuman/buat_pengumuman.html', context)

@login_required
def edit_pengumuman(request, id):
    context["id"] = id
    pengumuman = get_object_or_404(Pengumuman, id=id)
    if request.method == 'POST':
        form = PengumumanForm(request.POST or None, instance = pengumuman)
        user = User.objects.get(id = request.user.id)
        if request.POST and form.is_valid():
            judul = form.cleaned_data['judul']
            isi = form.cleaned_data['isi']
            pengumuman = Pengumuman.objects.filter(id=id).update(judul=judul, isi=isi)
            messages.success(request, 'Pengumuman berhasil diubah!')
            return redirect('pengumuman:pengumuman_saya')
        else:
            messages.error(request, 'Form tidak berhasil dibuat!')
            return redirect("pengumuman:buat_pengumuman")

    judul = pengumuman.judul
    isi = pengumuman.isi
    pengumuman_form = PengumumanForm(request.POST)
    pengumuman_form.fields["judul"].widget.attrs["value"] = judul
    pengumuman_form.fields["isi"].widget.attrs["value"] = isi
    context["form"] = pengumuman_form

    return render(request, 'pengumuman/edit_pengumuman.html', context)

@login_required
def hapus_pengumuman(request, id):
    pengumuman = get_object_or_404(Pengumuman, id=id)
    context["id"] = id
    if request.method == 'POST':
        pengumuman.delete()
        messages.success(request, 'Pengumuman berhasil dihapus!')
        return redirect('pengumuman:pengumuman_saya')
    return render(request, 'pengumuman/hapus_pengumuman.html', context)