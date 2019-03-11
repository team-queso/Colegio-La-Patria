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
def secundaria(request):
 	return render(request,"secundaria/base_secundaria.html")
def informacion_secundaria(request):
	return render(request,"secundaria/informacion_secundaria.html")
def horarios_secundaria(request):
	return render(request,"secundaria/horarios_secundaria.html")
def calificaciones_secundaria(request):
	return render(request,"secundaria/calificaciones_secundaria.html")
def reportes_secundaria(request):
	return render(request,"secundaria/reportes_secundaria.html")