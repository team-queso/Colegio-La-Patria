from django import forms

from .models import Alumno,Docente,Materia,Ciclo_escolar,UnidadCalificada


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
            'pin':'PIN',
            
        

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

class ingresarCiclo(forms.ModelForm):

    class Meta:
        model = Ciclo_escolar
            
        
        fields = [
        'clave',
        'descripcion',
        'fecha_inicio',
        'fecha_termino',
        'finalizado',
      
            
        ]
    
        labels ={

        'clave':'Clave',
        'descripcion':'Descripcion',
        'fecha_inicio':'Fecha de inicio',
        'fecha_termino': 'Fecha de terminación',
        'finalizado':'Activo',
        
        }
    
        widgets = {
        'clave': forms.TextInput(attrs={"class":'form-control'}),
        'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        'fecha inicio': forms.DateInput(attrs={'class':'form-control'}),
        'fecha termino': forms.DateInput(attrs={'class':'form-control'}),
        'finalizado': forms.CheckboxInput(attrs={'class':'form-control'}),
    
            }
class asignarCalificaciones(forms.ModelForm):

    class Meta:
        model = UnidadCalificada
            
        
        fields = [
        'unidad',
        'puntuacion_asignada',
        'alumno',

      
            
        ]
    
        labels ={

        'unidad':'Unidad-Materia',
        'puntuacion_asignada':'Calificación',
        'alumno':'Alumno',
        
        
        }
    
        widgets = {
        'unidad': forms.Select(attrs={"class":'form-control'}),
        'puntuacion_asignada': forms.TextInput(attrs={'class':'form-control'}),
        'alumno': forms.Select(attrs={'class':'form-control'}),

    
            }