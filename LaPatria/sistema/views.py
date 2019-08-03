from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, View
from sistema.forms import ingresarAlumno,ingresarDocente,ingresarMateria,ingresarCalificacion,ingresarAlumnoSecundaria,ingresarMateriaSecundaria,ingresarHorario
from sistema.models import Calificaciones,Alumno,Materia,Docente,AlumnoSecundaria,CalificacionesSecundaria,MateriaSecundaria,Horario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from sistema.utils import render_to_pdf
import pdfkit

def horario(request):
    template_name = 'primaria/horarios.html'
    return render(request, template_name)
def profesores(request):
	template_name2 = 'profesores/baseprofesores.html'
	return render(request, template_name2)

class MateriaCreate(LoginRequiredMixin, CreateView):
	model = Materia
	form_class = ingresarMateria
	template_name = 'panel_admin/ingresar_materia.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class MateriaSecundariaCreate(LoginRequiredMixin, CreateView):
	model = MateriaSecundaria
	form_class = ingresarMateriaSecundaria
	template_name = 'panel_admin/ingresar_materia_secundaria.html'
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
			
class AlumnosSecundariaList(LoginRequiredMixin, ListView):
	login_url = "/login/"
	redirect_field_name = "redirect_to"	
	queryset = AlumnoSecundaria.objects.all()
	template_name = 'panel_admin/listar_alumnos_secundaria.html'

	
	def get_queryset(self):
		queryset = self.request.GET.get("buscar")
		if queryset:
			q = AlumnoSecundaria.objects.filter(
				Q(no_control = queryset)
				).order_by('grado')
			return q 
		else:
			q = AlumnoSecundaria.objects.all()
			return q 	

class AlumnoSecundariaCreate(LoginRequiredMixin,CreateView):
	model = AlumnoSecundaria
	form_class = ingresarAlumnoSecundaria
	template_name = 'panel_admin/ingresar_alumno_secundaria.html'
	success_url = reverse_lazy("alumno:listar_alumnos_secundaria")

class AlumnosSecundariaUpdate(LoginRequiredMixin,UpdateView):
	model = AlumnoSecundaria
	form_class = ingresarAlumnoSecundaria
	template_name = 'panel_admin/editar_alumno_secundaria.html'
	success_url = reverse_lazy("alumno:listar_alumnos_secundaria")

class AlumnosSecundariaDelete(LoginRequiredMixin,DeleteView):
	model = AlumnoSecundaria
	template_name = 'panel_admin/eliminar_alumno_secundaria.html'
	success_url = reverse_lazy("alumno:listar_alumnos_secundaria")	

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
		

class PdfPrueba(View):
	def get(self, request, *args, **kwargs):
		
		datos ={
			"nombre" :  "jose",
			
		}
		pdf = render_to_pdf("panel_admin/imprimir.html",datos)
		return HttpResponse(pdf, content_type="application/pdf")
class HorarioCreate(CreateView):
	model = Horario
	form_class = ingresarHorario
	template_name = 'panel_admin/ingresar_horario.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class CalificacionDocenteCreate(LoginRequiredMixin,CreateView):
	model = Calificaciones
	form_class = ingresarCalificacion
	template_name = 'primaria/calificaciones.html'
	success_url = reverse_lazy("alumno:asignar_calificacion_docente")
