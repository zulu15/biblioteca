from django.urls import path
from django.views.generic import TemplateView
from .views import  *

urlpatterns = [
    path("inicio_autor/", TemplateView.as_view(template_name = "libro/autor/listar_autor.html"), name="inicio_autor"),
    path("crear_autor/",CrearAutor.as_view(), name = "crear_autor"),
    path("listar_autor/",ListarAutor.as_view(), name = "listar_autor"),
    path('editar_autor/<int:pk>', EditarAutor.as_view(), name="editar_autor"),
    path('eliminar_autor/<int:pk>', EliminarAutor.as_view(), name="eliminar_autor"),



    path("inicio_libro/", TemplateView.as_view(template_name = "libro/libro/listar_libro.html"), name = "inicio_libro"),
    path("listar_libro/",ListarLibro.as_view(), name = "listar_libro"),
    path("crear_libro/",CrearLibro.as_view(), name = "crear_libro"),
    path("editar_libro/<int:pk>",EditarLibro.as_view(), name = "editar_libro"),
    path('eliminar_libro/<int:pk>', EliminarLibro.as_view(), name="eliminar_libro"),
]
