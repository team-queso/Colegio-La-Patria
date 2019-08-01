from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, View
from sistema.forms import ingresarAlumno,ingresarDocente,ingresarMateria,ingresarCalificacion
from sistema.models import Calificaciones,Alumno,Materia,Docente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

import pdfkit

class MateriaCreate(CreateView):
	model = Materia
	form_class = ingresarMateria
	template_name = 'panel_admin/ingresar_materia.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class AlumnosList(LoginRequiredMixin, ListView):
	login_url = "/login/"
	redirect_field_name = "redirect_to"	
	queryset = Alumno.objects.all()
	template_name = 'panel_admin/listar_alumnos.html'

	
	def get_queryset(self):
		queryset = self.request.GET.get("buscar")
		if queryset:
			q = Alumno.objects.filter(
				Q(no_control = queryset)
				).order_by('grado')
			return q 
		else:
			q = Alumno.objects.all()
			return q 	

	
class AlumnoCreate(LoginRequiredMixin,CreateView):
	model = Alumno
	form_class = ingresarAlumno
	template_name = 'panel_admin/ingresar_alumno.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class AlumnosUpdate(LoginRequiredMixin,UpdateView):
	model = Alumno
	form_class = ingresarAlumno
	template_name = 'panel_admin/editar_alumno.html'
	success_url = reverse_lazy("alumno:listar_alumnos")


class AlumnosDelete(LoginRequiredMixin,DeleteView):
	model = Alumno
	template_name = 'panel_admin/eliminar_alumno.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class DocenteList(LoginRequiredMixin,ListView):			
	queryset = Docente.objects.all()
	template_name = 'panel_admin/listar_docente.html'
	
	def get_queryset(self):
		queryset = self.request.GET.get("buscar")
		if queryset:
			q = Docente.objects.filter(
				Q(pk = queryset)
				).order_by('grado')
			return q 
		else:
			q = Docente.objects.all()
			return q 	
class DocenteCreate(LoginRequiredMixin,CreateView):
	model = Docente
	form_class = ingresarDocente
	template_name = 'panel_admin/ingresar_docentes.html'
	success_url = reverse_lazy("alumno:listar_docente")

class DocenteUpdate(LoginRequiredMixin,UpdateView):
	model = Docente
	form_class = ingresarDocente
	template_name = 'panel_admin/editar_docente.html'
	success_url = reverse_lazy("alumno:listar_docente")

class DocenteDelete(LoginRequiredMixin,DeleteView):
	model = Docente
	template_name = 'panel_admin/eliminar_docente.html'
	success_url = reverse_lazy("alumno:listar_docente")

class CalificacionCreate(LoginRequiredMixin,CreateView):
	model = Calificaciones
	form_class = ingresarCalificacion
	template_name = 'panel_admin/calificaciones.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class CalificacionUpdate(LoginRequiredMixin,UpdateView):
	model = Calificaciones
	form_class = ingresarCalificacion
	template_name = 'panel_admin/editar_calificacion.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class CalificacionDelete(LoginRequiredMixin,DeleteView):
	model = Calificaciones
	template_name = 'panel_admin/eliminar_calificacion.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class CalificacionList(LoginRequiredMixin,ListView):
	Model = Calificaciones
	template_name = "panel_admin/listar.html"
	def get_queryset(self):
			q = Calificaciones.objects.filter(
				Q(alumno__no_control = self.kwargs['pk'])
				).order_by('grado')
			return q 
		



