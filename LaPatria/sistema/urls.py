from django.urls import path

from sistema import views

urlpatterns = [
    
   
    path('informacion', views.informacion, name='informacion'),
    path('horarios', views.horarios, name='horarios'),
    path('calificaciones', views.calificaciones, name='calificaciones'),
    path('reportes', views.reportes, name='reportes'),
    path('profesores', views.profe, name='profes'),
    path('administrador', views.panel_administrador, name='administrador'),
    path('administrador/ingresar-alumno', views.panel_administrador_ingresar_alumno, name='ingresar_alumno'),
    path('administrador/ingresar-materia', views.panel_administrador_ingresar_materia, name='ingresar_materia'),
    path('administrador/asignar-grupos', views.panel_administrador_asignar_grupos, name='asignar_grupos'),
    ]