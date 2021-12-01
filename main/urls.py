from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.profil, name='home'),
    path('profil', views.profil, name='profil'),
    path('profil/edit', views.profil_edit, name='profil_edit'),
    path('presensi', views.presensi, name='presensi'),
    path('presensi/add', views.presensi_edit, name='presensi_edit'),
]
