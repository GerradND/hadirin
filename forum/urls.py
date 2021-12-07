from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_thread, name='add_thread'),
    path('<int:pk>/', views.thread_detail, name='detail_thread'),
    path('<int:pk>/edit/', views.edit_thread, name='edit_thread'),
    path('<int:pk>/reply/', views.reply_thread, name='reply_thread'),
    path('<int:pk>/delete/', views.delete_thread, name='delete_thread'),
]