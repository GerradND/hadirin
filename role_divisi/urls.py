from django.urls import path
from .views import IndexView, AddRoleDivisiView, EditRoleDivisiView, DeleteRoleDivisiView

app_name = 'role_divisi'

urlpatterns = [
    path('', IndexView.as_view(), name='role_divisi_list'),
    path('tambah/', AddRoleDivisiView.as_view(), name='add_role_divisi'),
    path('ubah/', EditRoleDivisiView.as_view(), name='edit_role_divisi'),
    path('hapus/', DeleteRoleDivisiView.as_view(), name='delete_role_divisi')
]
