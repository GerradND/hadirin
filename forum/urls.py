from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_thread, name='add_thread'),
    path('1/', views.thread_detail, name='detail'),
    path('1/edit', views.edit_thread, name='edit_thread'),
]