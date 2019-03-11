from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('primaria/', views.primaria, name='primaria'),
    path('primaria/informacion', views.informacion, name='primaria'),
]