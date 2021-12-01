from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import RoleDivisi
from django.urls import reverse_lazy


class IndexView(ListView):
    model = RoleDivisi


class AddRoleDivisiView(CreateView):
    model = RoleDivisi
    fields = '__all__'
    template_name_suffix = "_add_form"


class EditRoleDivisiView(UpdateView):
    model = RoleDivisi
    fields = ['keterangan']
    template_name_suffix = "_edit_form"


class DeleteRoleDivisiView(DeleteView):
    model = RoleDivisi
    success_url = reverse_lazy('role-divisi-list')
