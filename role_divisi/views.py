from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import RoleDivisi
from django.urls import reverse_lazy
from django.shortcuts import redirect


class BaseRoleDivisiView(LoginRequiredMixin, UserPassesTestMixin):
    model = RoleDivisi
    fields = '__all__'
    context_object_name = "role_divisi"

    def test_func(self):
        return self.request.user.is_superuser

    def get_permission_denied_message(self):
        return f"User {self.request.user} bukan seorang admin"

    def handle_no_permission(self):
        return redirect('main:home')


class IndexView(BaseRoleDivisiView, ListView):
    context_object_name = 'role_divisi_list'
    template_name = "role_divisi/index.html"


class DetailRoleDivisiView(BaseRoleDivisiView, DetailView):
    template_name = "role_divisi/detail.html"


class AddRoleDivisiView(BaseRoleDivisiView, CreateView):
    template_name = "role_divisi/add_form.html"

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, f"Role Divisi {self.object.nama} berhasil ditambahkan!")
        return reverse_lazy("role_divisi:role_divisi_list")


class EditRoleDivisiView(BaseRoleDivisiView, UpdateView):
    template_name = "role_divisi/edit_form.html"

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, f"Role Divisi {self.object.nama} berhasil diubah!")
        return reverse_lazy("role_divisi:role_divisi_list")


class DeleteRoleDivisiView(BaseRoleDivisiView, DeleteView):
    template_name = "role_divisi/confirm_delete.html"

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, f"Role Divisi {self.object.nama} berhasil dihapus!")
        return reverse_lazy("role_divisi:role_divisi_list")
