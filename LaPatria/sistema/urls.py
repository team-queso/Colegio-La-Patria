from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('primaria/', views.primaria, name='primaria'),
    path('primaria/informacion', views.informacion, name='informacion'),
    path('primaria/horarios', views.horarios, name='horarios'),
    path('primaria/calificaciones', views.calificaciones, name='calificaciones'),



]