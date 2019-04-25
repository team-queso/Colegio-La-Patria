from django import forms

from .models import Alumno,Materia,Reticula


class ingresarAlumno(forms.ModelForm):

    class Meta:
        model = Alumno

        fields = [
            'nombre',
            'telefono',
            'domicilio',
            'pin',
            
        ]

        labels ={
            'nombre':'Nombre',
            'telefono':'Telefono',
            'domicilio': 'Domicilio',
            'pin':'PIN',
        

        }

        widgets = {
            'nombre': forms.TextInput(attrs={"class":'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.TextInput(attrs={'class':'form-control'}),
        

                 }
class ingresarMateria(forms.ModelForm):
    class Meta:
        model = Materia

        fields = [
            'materia',
            'claveMateria',
            
        ]

        labels ={
            'materia':'Materia',
            'claveMateria':'Clave de la Materia',
            

        }

        widgets = {
            'materia': forms.TextInput(attrs={"class":'form-control'}),
            'claveMateria': forms.TextInput(attrs={'class':'form-control'}),
            

                 }
class asignarMateria(forms.ModelForm):
    class Meta:
        model = Reticula

        fields = [
            'anio_reticula',
            'materiaAsignada',
            'grupoAsignado',
            'cicloEscolar',
            
        ]

        labels ={
            'anio_reticula':'Año',
            'grupoAsignado':'Grupo',
            'materiaAsignada': 'Materias',
            'cicloEscolar': 'Periodo escolar',
            

        }

        widgets = {
            'anio_reticula': forms.TextInput(attrs={'class':'form-control'}),
            'materiaAsignada': forms.Select(attrs={'class':'form-control'}),
            'grupoAsignado': forms.Select(attrs={"class":'form-control'}),
            'cicloEscolar': forms.Select(attrs={"class":'form-control'}),

                 }