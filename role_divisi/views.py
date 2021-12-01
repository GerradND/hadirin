from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import RoleDivisi
from django.urls import reverse_lazy


class IndexView(ListView):
    model = RoleDivisi
    template_name = "role_divisi/index.html"


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
    success_url = reverse_lazy('role-divisi-list')
    template_name = "role_divisi/confirm_delete.html"
