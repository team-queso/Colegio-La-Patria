from django.urls import path

from registros import views


urlpatterns = [
path('', views.index, name='index'),
path('administrador/', views.login_administrador, name='login_administrador'),

]