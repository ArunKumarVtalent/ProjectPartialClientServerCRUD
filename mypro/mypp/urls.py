from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('home/', views.Home, name='homepage'),
    path('create/', views.Create, name='create'),
    path('edit/', views.Edit, name='edit'),
    path('delete/', views.Delete, name='delete')
]