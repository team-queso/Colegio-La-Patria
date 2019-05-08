from django import forms

from .models import Alumno,Materia,Reticula,Docente


class ingresarAlumno(forms.ModelForm):

    class Meta:
        model = Alumno

        fields = [
            'nombre',
            'telefono',
            'domicilio',
            'pin',
            'reticula',
            
        ]

        labels ={
            'nombre':'Nombre',
            'telefono':'Telefono',
            'domicilio': 'Domicilio',
            'pin':'PIN',
            'reticula':'Grupo'
        

        }

        widgets = {
            'nombre': forms.TextInput(attrs={"class":'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.TextInput(attrs={'class':'form-control'}),
            'reticula': forms.Select(attrs={"class":'form-control'}),
        

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
            'periodo',
            'materiaAsignada',
            'grupoAsignado',
          
            
        ]

        labels ={
            'periodo':'Periodo',
            'materiaAsignada': 'Materias',
            'grupoAsignado':'Grupo',
            
            
            

        }

        widgets = {
            'periodo': forms.TextInput(attrs={'class':'form-control'}),
            'materiaAsignada': forms.Select(attrs={'class':'form-control'}),
            'grupoAsignado': forms.Select(attrs={"class":'form-control'}),
            
                 }
class ingresarDocente(forms.ModelForm):
    class Meta:
        model = Docente
        
        fields = [
        'nombreDocente',
        'correo',
        'telefono',
        'domicilio',
        'registro',
        'pin',
            
        ]
    
        labels ={

        'nombreDocente':'Nombre Docente',
        'correo':'Correo',
        'telefono':'Telefono',
        'domicilio': 'Domicilio',
        'registro':'Cedula',
        'pin':'PIN',
        }
    
        widgets = {
        'nombreDocente': forms.TextInput(attrs={"class":'form-control'}),
        'correo': forms.TextInput(attrs={'class':'form-control'}),
        'telefono': forms.TextInput(attrs={'class':'form-control'}),
        'domicilio': forms.TextInput(attrs={'class':'form-control'}),
        'registro': forms.TextInput(attrs={'class':'form-control'}),
        'pin': forms.TextInput(attrs={'class':'form-control'}),
            }