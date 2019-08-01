from django.urls import path
from django.contrib.auth.decorators import login_required
from sistema.views import *


app_name = 'alumno'  
urlpatterns = [
    
    
   
    
    path('administrador/ingresar-alumno', AlumnoCreate.as_view() , name='ingresar_alumno'),
    path('administrador/ingresar-materia', MateriaCreate.as_view(), name='ingresar_materia'),
    path('administrador/ingresar-docente',DocenteCreate.as_view(), name='ingresar_docente'),
    path('administrador/calificacion', CalificacionCreate.as_view(), name='asignar_calificaciones'),
    path('administrador/listar/<int:pk>', CalificacionList.as_view(), name='listar'),
    path('administrador/listar-docente', DocenteList.as_view(), name='listar_docente'),
    path('administrador/listar-alumnos', AlumnosList.as_view() , name='listar_alumnos'),
    path('administrador/editar-calificacion/<int:pk>', CalificacionUpdate.as_view(), name='editar_calificacion'),
    path('administrador/eliminar-calificacion/<int:pk>', CalificacionDelete.as_view(), name='eliminar_calificacion'),
    path('administrador/editar-alumno/<int:pk>', AlumnosUpdate.as_view(), name='editar_alumno'),
    path('administrador/eliminar-alumno/<int:pk>', AlumnosDelete.as_view(), name='eliminar_alumno'),
    path('administrador/editar-docente/<int:pk>', DocenteUpdate.as_view(), name='editar_docente'),
    path('administrador/eliminar-docente/<int:pk>', DocenteDelete.as_view(), name='eliminar_docente'),
    ]