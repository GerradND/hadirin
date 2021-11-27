from django.urls import path
from . import views

app_name = 'perizinan'

urlpatterns = [
    path('', views.index, name='index'),
]