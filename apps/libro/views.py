from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AutorForm, LibroForm
from .models import Autor, Libro


# Empiezan las vistas del modelo Autor

class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class ListarAutor(LoginRequiredMixin, ListView):
    template_name = 'libro/autor/listar_autor.html'
    model = Autor
    context_object_name = "autores"
    queryset = Autor.objects.filter(estado = True).order_by('-pk')


class EditarAutor(LoginRequiredMixin, UpdateView):
    template_name = 'libro/autor/editar_autor.html'
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")

class EliminarAutor(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = reverse_lazy("libro:listar_autor")
    def post(self, request, pk, *args, **kargs):
        object = get_object_or_404(self.model, pk = pk)
        object.estado = False
        object.save()
        return redirect(self.success_url)


class CrearAutor(CreateView):
    form_class = AutorForm
    model = Autor
    success_url = reverse_lazy("libro:listar_autor")
    template_name = "libro/autor/crear_autor.html"



# Empiezan las vistas del modelo Libro

class ListarLibro(LoginRequiredMixin,ListView):
    model = Libro
    template_name = "libro/libro/listar_libro.html"
    form_class = LibroForm
    queryset = Libro.objects.filter(estado = True).order_by('-pk')



class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy("libro:listar_libro")


class EditarLibro(LoginRequiredMixin,UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = "libro/libro/editar_libro.html"
    success_url = reverse_lazy("libro:listar_libro")



class EliminarLibro(LoginRequiredMixin,DeleteView):
    model = Libro
    success_url = reverse_lazy("libro:listar_libro")

    def post(self,request,pk,*arg,**kargs):
        object = get_object_or_404(self.model, pk = pk)
        object.estado = False
        object.save()
        return redirect(self.success_url)
