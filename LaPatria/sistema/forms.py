from django import forms
from django.db.models import Q
from .models import Alumno,Docente,Materia,Calificaciones,AlumnoSecundaria,MateriaSecundaria

class ingresarAlumno(forms.ModelForm):

    class Meta:
        model = Alumno

        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'telefono',
            'domicilio',
            'pin',
        
            
            
        ]

        labels ={
            'nombre':'Nombre',
            'apellido_paterno':'Apellido Paterno',
            'apellido_materno':'Apelldio Materno',
            'telefono':'Telefono',
            'domicilio': 'Domicilio',
            'pin':'Grado',
            
        

        }

        widgets = {
            'nombre': forms.TextInput(attrs={"class":'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={"class":'form-control'}),
            'apellido_materno': forms.TextInput(attrs={"class":'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.TextInput(attrs={'class':'form-control'}),
            
            
        

                 }
class ingresarMateria(forms.ModelForm):
    class Meta:
        model = Materia

        fields = [
            'nombreMateria',
            'clave',
            
        ]

        labels ={
            'nombreMateria':'Materia',
            'clave':'Clave de la Materia',
            

        }

        widgets = {
            'nombreMateria': forms.TextInput(attrs={"class":'form-control'}),
            'clave': forms.TextInput(attrs={'class':'form-control'}),
            

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
      
            
        ]
    
        labels ={

        'nombreDocente':'Nombre Docente',
        'correo':'Correo',
        'telefono':'Telefono',
        'domicilio': 'Domicilio',
        'registro':'Cedula',
        
        }
    
        widgets = {
        'nombreDocente': forms.TextInput(attrs={"class":'form-control'}),
        'correo': forms.TextInput(attrs={'class':'form-control'}),
        'telefono': forms.TextInput(attrs={'class':'form-control'}),
        'domicilio': forms.TextInput(attrs={'class':'form-control'}),
        'registro': forms.TextInput(attrs={'class':'form-control'}),
    
            }

class ingresarCalificacion(forms.ModelForm):

    
    class Meta:
        model = Calificaciones
        
        fields = [
        'alumno',
        'materia',
        'grado',
        'Unidad1',
        'Unidad2',
        'Unidad3',
        'Unidad4',
        'Unidad5',
    
      
            
        ]
    
        labels ={
        'alumno':'No_Control',
        'materia':'Materia',
        'grado': 'Grado',
        'Unidad1':'Unidad 1',
        'Unidad2':'Unidad 2',
        'Unidad3':'Unidad 3',
        'Unidad4':'Unidad 4',
        'Unidad5':'Unidad 5',
        

        
        }
    
        widgets = {
        'alumno': forms.TextInput(attrs={'class':'form-control'}),
        'materia': forms.Select(attrs={'class':'form-control'}),
        'grado'  : forms.TextInput(attrs={'class':'form-control'}),
        'Unidad1': forms.TextInput(attrs={'class':'form-control'}),
        'Unidad2': forms.TextInput(attrs={'class':'form-control'}),
        'Unidad3': forms.TextInput(attrs={'class':'form-control'}),
        'Unidad4': forms.TextInput(attrs={'class':'form-control'}),
        'Unidad5': forms.TextInput(attrs={'class':'form-control'}),
        
        
    
            }

class ingresarAlumnoSecundaria(forms.ModelForm):


    class Meta:
        model = AlumnoSecundaria

        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'telefono',
            'domicilio',

        
            
            
        ]

        labels ={
            'nombre':'Nombre',
            'apellido_paterno':'Apellido Paterno',
            'apellido_materno':'Apelldio Materno',
            'telefono':'Telefono',
            'domicilio': 'Domicilio',
       
            
        

        }

        widgets = {
            'nombre': forms.TextInput(attrs={"class":'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={"class":'form-control'}),
            'apellido_materno': forms.TextInput(attrs={"class":'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            
            
        

                 }
class ingresarMateriaSecundaria(forms.ModelForm):
    class Meta:
        model = MateriaSecundaria

        fields = [
            'nombreMateria',
            'clave',
            
        ]

        labels ={
            'nombreMateria':'Materia',
            'clave':'Clave de la Materia',
            

        }

        widgets = {
            'nombreMateria': forms.TextInput(attrs={"class":'form-control'}),
            'clave': forms.TextInput(attrs={'class':'form-control'}),
            

                 }