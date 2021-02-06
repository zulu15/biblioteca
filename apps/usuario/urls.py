from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import  CrearUsuario, ListarUsuario, EliminarUsuario, EditarUsuario, InicioUsuario

urlpatterns = [
    path("inicio_usuario/",InicioUsuario.as_view(), name="inicio_usuario"),
    path("listar_usuario/",ListarUsuario.as_view(), name = "listar_usuario"),
    path("crear_usuario/",CrearUsuario.as_view(), name = "crear_usuario"),
    path("eliminar_usuario/<int:pk>",EliminarUsuario.as_view(), name = "eliminar_usuario"),
    path("editar_usuario/<int:pk>",EditarUsuario.as_view(), name = "editar_usuario"),



]


