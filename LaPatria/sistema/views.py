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
