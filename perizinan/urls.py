from django.urls import path
from . import views

app_name = 'perizinan'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_izin, name='add_izin'),
    path('validasi', views.validasi_izin, name='validasi_izin'),
    path('validasi/detail/<int:id>', views.detail_izin, name='detail_izin'),
]