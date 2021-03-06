from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import  *

urlpatterns = [
    #vistas para autor    
    path("crear_autor/",CrearAutor.as_view(), name = "crear_autor"),
    path("listar_autor/",ListarAutor.as_view(), name = "listar_autor"),
    path('editar_autor/<int:pk>', EditarAutor.as_view(), name="editar_autor"),
    path('eliminar_autor/<int:pk>', EliminarAutor.as_view(), name="eliminar_autor"),

    #vistas para libro
    path("listar_libro/",ListarLibro.as_view(), name = "listar_libro"),
    path("crear_libro/",CrearLibro.as_view(), name = "crear_libro"),
    path("editar_libro/<int:pk>",EditarLibro.as_view(), name = "editar_libro"),
    path('eliminar_libro/<int:pk>', EliminarLibro.as_view(), name="eliminar_libro"),
    path('detalle_libro/<int:pk>', DetalleLibroDisponible.as_view(), name="detalle_libro"),
]

urlpatterns += [
    path("inicio_autor/", InicioAutor.as_view(), name="inicio_autor"),
    path("inicio_libro/", InicioLibro.as_view(), name = "inicio_libro"),
    
]