from django.urls import path
from .views import add_role_divisi, edit_role_divisi, index, delete_role_divisi, role_divisi_detail

app_name = 'role_divisi'

urlpatterns = [
    path('', index, name='role_divisi_list'),
    path('1/', role_divisi_detail, name='detail_role_divisi'),
    path('tambah/', add_role_divisi, name='add_role_divisi'),
    path('ubah/1/', edit_role_divisi, name='edit_role_divisi'),
    path('hapus/1/', delete_role_divisi, name='delete_role_divisi')
]
