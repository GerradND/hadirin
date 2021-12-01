from django.urls import path
from .views import IndexView, AddRoleDivisiView, EditRoleDivisiView, DeleteRoleDivisiView

app_name = 'role_divisi'

urlpatterns = [
    path('', IndexView.as_view(), name='role-divisi-list'),
    path('add/', AddRoleDivisiView.as_view(), name='add-role-divisi'),
    path('edit/', EditRoleDivisiView.as_view(), name='edit-role-divisi'),
    path('delete/', DeleteRoleDivisiView.as_view(), name='delete-role-divisi')
]
