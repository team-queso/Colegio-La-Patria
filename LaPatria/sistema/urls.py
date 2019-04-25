from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('inicio/', views.primaria, name='primaria'),
    path('colegiolapatria/informacion', views.informacion, name='informacion'),
    path('colegiolapatria/horarios', views.horarios, name='horarios'),
    path('colegiolapatria/calificaciones', views.calificaciones, name='calificaciones'),
    path('colegiolapatria/reportes', views.reportes, name='reportes'),
    path('colegiolapatria/profesores', views.profe, name='profes'),
    path('colegiolapatria/administrador', views.panel_administrador, name='administrador'),
    path('colegiolapatria/administrador/ingresar-alumno', views.panel_administrador_ingresar_alumno, name='ingresar_alumno'),
    path('colegiolapatria/administrador/ingresar-materia', views.panel_administrador_ingresar_materia, name='ingresar_materia'),
    ]