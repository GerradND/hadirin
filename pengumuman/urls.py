from django.urls import path
from . import views

app_name = 'pengumuman'

urlpatterns = [
    path('', views.pengumuman, name='pengumuman'),
    path('pengumuman_saya/', views.pengumuman_saya, name='pengumuman_saya'),
    path('buat_pengumuman/', views.buat_pengumuman, name='buat_pengumuman'),
    path('edit_pengumuman/<int:id>', views.edit_pengumuman, name='edit_pengumuman'),
    path('hapus_pengumuman/<int:id>', views.hapus_pengumuman, name='hapus_pengumuman'),
]