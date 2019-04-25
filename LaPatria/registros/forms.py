from django import forms

from sistema.models import administrador

class Login_admin(forms.ModelForm):
    class Meta:
        model = administrador

        fields = [
            'usuario',
            'password',
        ]

        labels ={
            'usuario':'Usuario',
            'password':'Contraseña',
          
            

        }

        widgets = {
            'usuario': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            

                 }

