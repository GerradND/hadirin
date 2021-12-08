from django.urls import path
from .views import IndexView, DetailRoleDivisiView, AddRoleDivisiView, EditRoleDivisiView, DeleteRoleDivisiView

app_name = 'role_divisi'

urlpatterns = [
    path('', IndexView.as_view(), name='role_divisi_list'),
    path('<int:pk>/', DetailRoleDivisiView.as_view(), name='detail_role_divisi'),
    path('tambah/', AddRoleDivisiView.as_view(), name='add_role_divisi'),
    path('ubah/<int:pk>/', EditRoleDivisiView.as_view(), name='edit_role_divisi'),
    path('hapus/<int:pk>/', DeleteRoleDivisiView.as_view(), name='delete_role_divisi')
]
