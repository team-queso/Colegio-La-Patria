from django import forms

from .models import Alumno,Materia


class ingresarAlumno(forms.ModelForm):

    class Meta:
        model = Alumno

        fields = [
            'nombre',
            'telefono',
            'domicilio',
            'pin',
            'grupoAsignado'
        ]

        labels ={
            'nombre':'Nombre',
            'telefono':'Telefono',
            'domicilio': 'Domicilio',
            'pin':'PIN',
            'grupoAsignado': 'Grupo'

        }

        widgets = {
            'nombre': forms.TextInput(attrs={"class":'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.TextInput(attrs={'class':'form-control'}),
            'grupo': forms.Select(attrs={'class':'form-control'}),

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