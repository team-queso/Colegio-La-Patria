from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request,"index.html")
def login_administrador(request):
        loginAdmin = Login_admin(request.POST)
        if loginAdmin.is_valid():
            data = loginAdmin.cleaned_data
            usuario = data.get("usuario")
            contraseña = data.get("pass")
            accesso = authenticate(username=usuario,password=contraseña)
            if accesso is not None:
                login(request,accesso)
                return HttpResponse("Bienvenido")
            else:
                return HttpResponse("Usuario / Contraseña incorrectos")
        else:
            loginAdmin = Login_admin()

        return render(request,"registration/login_administrador.html", {'loginAdmin': loginAdmin})
    