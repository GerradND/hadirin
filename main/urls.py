from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('profil', views.profil, name='profil'),
    path('profil/edit', views.profil_edit, name='profil_edit')
]
