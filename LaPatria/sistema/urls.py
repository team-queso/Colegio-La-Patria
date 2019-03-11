from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('primaria/', views.primaria, name='primaria'),
    path('primaria/informacion', views.informacion, name='informacion'),
    path('primaria/horarios', views.horarios, name='horarios'),
    path('primaria/calificaciones', views.calificaciones, name='calificaciones'),
    path('primaria/reportes', views.reportes, name='reportes'),
    path('secundaria/', views.secundaria, name='secundaria'),
    path('secundaria/informacion', views.informacion_secundaria, name='informacion2'),
    path('secundaria/horarios', views.horarios_secundaria, name='horarios2'),
    path('secundaria/calificaciones', views.calificaciones_secundaria, name='calificaciones2'),
    path('secundaria/reportes', views.reportes_secundaria, name='reportes2'),


]