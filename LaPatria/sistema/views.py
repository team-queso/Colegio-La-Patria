from django.shortcuts import render,redirect
from django.http import HttpResponse

from sistema.forms import ingresarAlumno,ingresarMateria,asignarMateria,ingresarDocente
from sistema.models import Alumno


def primaria(request):
 	return render(request,"primaria/base.html")
def informacion(request):
	return render(request,"primaria/informacion.html")
def horarios(request):
	return render(request,"primaria/horarios.html")
def calificaciones(request):
	return render(request,"primaria/calificaciones.html")
def reportes(request):
	return render(request,"primaria/reportes.html")
def profe(request):
	return render(request,"profesores/baseprofesores.html")
def panel_administrador(request):
	return render(request,"panel_admin/baseadmin.html")
def panel_administrador_ingresar_alumno(request):
	if request.method == 'POST':
		formularioAlumno = ingresarAlumno(request.POST)
		if formularioAlumno.is_valid():
			formularioAlumno.save()
	else:
		formularioAlumno = ingresarAlumno()

		return render(request,"panel_admin/ingresar_alumno.html", {'formularioAlumno': formularioAlumno })

def panel_administrador_ingresar_materia(request):
	if request.method == 'POST':
		formularioMateria = ingresarMateria(request.POST)
		if formularioMateria.is_valid():
			formularioMateria.save()
	else:
		formularioMateria = ingresarMateria()

		return render(request,"panel_admin/ingresar_materia.html", {'formularioMateria': formularioMateria })
def panel_administrador_ingresar_docente(request):
	if request.method == 'POST':
		ingresarDocenteV = ingresarDocente(request.POST)
		if ingresarDocenteV.is_valid():
			ingresarDocenteV.save()
	else:
		ingresarDocenteV = ingresarDocente()

		return render(request,"panel_admin/ingresar_docentes.html", {'ingresarDocenteV': ingresarDocenteV })
def panel_administrador_asignar_grupos(request):
	if request.method == 'POST':
		formularioAsignarMateria = asignarMateria(request.POST)
		if formularioAsignarMateria.is_valid():
			formularioAsignarMateria.save()
	else:
		formularioAsignarMateria = asignarMateria()

		return render(request,"panel_admin/asignar_grupos.html", {'formularioAsignarMateria': formularioAsignarMateria })

def listarAlumno(request):
	alumno = Alumno.objects.all()
	contexto = {"alumnos" : alumno}
	return render(request,'panel_admin/listar.html',contexto)

def panel_administrador_editar(request,no_control):
	alumno = Alumno.objects.get(pk = no_control)
	if request.method == 'GET':
		formularioAlumno=ingresarAlumno(instance = alumno)
	else:
		formularioAlumno=ingresarAlumno(request.POST, instance=alumno)
		if formularioAlumno.is_valid():
			formularioAlumno.save()
			return redirect(listarAlumno)
	return render(request,'panel_admin/reinscripcion.html',{'formularioAlumno':formularioAlumno})