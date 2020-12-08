from django.urls import path
from .views import list_cadastro, create_cadastro, update_cadastro, delete_cadastro

urlpatterns = [
    path('', list_cadastro, name='list_cadastro'),
    path('new', create_cadastro, name='create_cadastro'),
    path('update/<int:id>/', update_cadastro, name='update_cadastro'),
    path('delete/<int:id>/', delete_cadastro, name='delete_cadastro'),
]
