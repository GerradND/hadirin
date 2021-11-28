from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.home, name='home'),
    path('1/', views.thread_detail, name='detail'),
]