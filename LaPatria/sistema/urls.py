from django.urls import path
from django.contrib.auth.decorators import login_required
from sistema.views import *


app_name = 'alumno'  
urlpatterns = [
    
    
    path("profesores/", profesores, name="profesores"),
    path("profesores/horario/", horario , name="horario"),
    path("profesores/calificar/", CalificacionDocenteCreate.as_view(),name="asignar_calificacion_docente"),

    path('administrador/ingresar-horario', HorarioCreate.as_view() , name='ingresar_horario'),

    path('administrador/imprimir', PdfPrueba.as_view(), name='imprimir'),
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

    path('administrador/ingresar-materia-secundaria', MateriaSecundariaCreate.as_view(), name='ingresar_materia_secundaria'),

    path('administrador/listar-alumnos-secundaria', AlumnosSecundariaList.as_view() , name='listar_alumnos_secundaria'),
    path('administrador/ingresar-alumno-secundaria', AlumnoSecundariaCreate.as_view() , name='ingresar_alumno_secundaria'),
    path('administrador/editar-alumno-secundaria/<int:pk>', AlumnosSecundariaUpdate.as_view(), name='editar_alumno_secundaria'),
    path('administrador/eliminar-alumno-secundaria/<int:pk>', AlumnosSecundariaDelete.as_view(), name='eliminar_alumno_secundaria'),

    path('administrador/calificacion-secundaria', CalificacionSecundariaCreate.as_view(), name='asignar_calificaciones_secundaria'),
    path('administrador/listar-calificacion-secundaria/<int:pk>', CalificacionSecundariaList.as_view(), name='listar_calificaciones_secundaria'),
    path('administrador/editar-calificacion-secundaria/<int:pk>', CalificacionSecundariaUpdate.as_view(), name='editar_calificacion_secundaria'),
    path('administrador/eliminar-calificacion-secundaria/<int:pk>', CalificacionSecundariaDelete.as_view(), name='eliminar_calificacion_secundaria'),

    path('administrador/ingresar-docente-secundaria',DocenteSecundariaCreate.as_view(), name='ingresar_docente_secundaria'),
    path('administrador/listar-docente-secundaria', DocenteSecundariaList.as_view(), name='listar_docente_secundaria'),
    path('administrador/editar-docente-secundaria/<int:pk>', DocenteSecundariaUpdate.as_view(), name='editar_docente_secundaria'),
    path('administrador/eliminar-docente-secundaria/<int:pk>', DocenteSecundariaDelete.as_view(), name='eliminar_docente_secundaria'),
    
    path('administrador/listar-horario', HorarioList.as_view(), name='listar_horario'),
    ]