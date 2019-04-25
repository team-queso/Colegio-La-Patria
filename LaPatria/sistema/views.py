from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")
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
	return render(request,"profe/basepro.html")
def panel_administrador(request):
	return render(request,"panel_admin/baseadmin.html")
def panel_administrador_ingresar_alumno(request):
	return render(request,"panel_admin/ingresar_alumno.html")
def panel_administrador_ingresar_materia(request):
	return render(request,"panel_admin/ingresar_materia.html")
