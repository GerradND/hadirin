from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import RoleDivisi
from django.urls import reverse_lazy


class IndexView(ListView):
    model = RoleDivisi
    template_name = "role_divisi/index.html"


class DetailRoleDivisiView(DetailView):
    model = RoleDivisi
    template_name = "role_divisi/detail.html"


class AddRoleDivisiView(CreateView):
    model = RoleDivisi
    fields = '__all__'
    template_name = "role_divisi/add_form.html"


class EditRoleDivisiView(UpdateView):
    model = RoleDivisi
    fields = ['keterangan']
    template_name = "role_divisi/edit_form.html"


class DeleteRoleDivisiView(DeleteView):
    model = RoleDivisi
    success_url = reverse_lazy('role_divisi_list')
    template_name = "role_divisi/confirm_delete.html"


def index(request):
    return render(request, 'role_divisi/index.html')


def role_divisi_detail(request):
    return render(request, 'role_divisi/detail.html')


def add_role_divisi(request):
    return render(request, 'role_divisi/add_form.html')


def edit_role_divisi(request):
    return render(request, 'role_divisi/edit_form.html')


def delete_role_divisi(request):
    return render(request, 'role_divisi/confirm_delete.html')
