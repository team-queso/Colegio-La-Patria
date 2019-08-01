from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, View
from sistema.forms import ingresarAlumno,ingresarDocente,ingresarMateria,ingresarCalificacion
from sistema.models import Calificaciones,Alumno,Materia,Docente





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

def panel_administrador_ingresar_ciclo(request):
	if request.method == 'POST':
		formularioCiclo = ingresarCiclo(request.POST)
		if formularioCiclo.is_valid():
			formularioCiclo.save()
	else:
		formularioCiclo = ingresarCiclo()

		return render(request,"panel_admin/ciclo_escolar.html", {'formularioCiclo': formularioCiclo })
			


"""def panel_administrador_asignar_calificacion(request):
		materia = Materia.objects.filter(Q(grado = 2))
		contexto = {"materias" : materia} 
		return render(request,"panel_admin/calificaciones.html", contexto)"""

"""def panel_administrador_calificar(request):
	if request.method == 'POST':
		form = ingresarCalificacion(request.POST)
		if form.is_valid():
			form.save()
		else:
			form = ingresarCalificacion()

			return render(request,"panel_admin/calificaciones.html", form)"""		



class AlumnosList(ListView):			
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
		
class AlumnoCreate(CreateView):
	model = Alumno
	form_class = ingresarAlumno
	template_name = 'panel_admin/ingresar_alumno.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class AlumnosUpdate(UpdateView):
	model = Alumno
	form_class = ingresarAlumno
	template_name = 'panel_admin/editar_alumno.html'
	success_url = reverse_lazy("alumno:listar_alumnos")


class AlumnosDelete(DeleteView):
	model = Alumno
	template_name = 'panel_admin/eliminar_alumno.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class DocenteList(ListView):			
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
class DocenteCreate(CreateView):
	model = Docente
	form_class = ingresarDocente
	template_name = 'panel_admin/ingresar_docentes.html'
	success_url = reverse_lazy("alumno:listar_docente")

class DocenteUpdate(UpdateView):
	model = Docente
	form_class = ingresarDocente
	template_name = 'panel_admin/editar_docente.html'
	success_url = reverse_lazy("alumno:listar_docente")

class DocenteDelete(DeleteView):
	model = Docente
	template_name = 'panel_admin/eliminar_docente.html'
	success_url = reverse_lazy("alumno:listar_docente")

class CalificacionCreate(CreateView):
	model = Calificaciones
	form_class = ingresarCalificacion
	template_name = 'panel_admin/calificaciones.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class CalificacionUpdate(UpdateView):
	model = Calificaciones
	form_class = ingresarCalificacion
	template_name = 'panel_admin/editar_calificacion.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class CalificacionDelete(DeleteView):
	model = Calificaciones
	template_name = 'panel_admin/eliminar_calificacion.html'
	success_url = reverse_lazy("alumno:listar_alumnos")

class CalificacionList(ListView):
	Model = Calificaciones
	template_name = "panel_admin/listar.html"
	def get_queryset(self):
			q = Calificaciones.objects.filter(
				Q(alumno__no_control = self.kwargs['pk'])
				).order_by('grado')
			return q 
		


	"""def get_queryset(self, no_control):
		queryset = self.request.GET.get('no_control')
		if queryset:
			q = Calificaciones.objects.filter(
				Q(alumno__Alumno_no_control = queryset)
				).order_by('grado')
			return q 
		else:
			q = Calificaciones.objects.all()
			return q"""