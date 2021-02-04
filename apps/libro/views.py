from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse

from .forms import AutorForm, LibroForm
from .models import Autor, Libro


# Empiezan las vistas del modelo Autor

class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class ListarAutor(LoginRequiredMixin, ListView):
    model = Autor
    
    def get(self, request, *args, **kargs):
        if request.is_ajax():
            listado_autor = Autor.objects.filter(estado = True).order_by('-pk')
            return HttpResponse(serialize("json", listado_autor), "application/json")

        else:
            return redirect("libro:inicio_autor")    


class EditarAutor(LoginRequiredMixin, UpdateView):
    template_name = 'libro/autor/editar_autor.html'
    model = Autor
    form_class = AutorForm

    def post(self, request, *args, **kargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f"Se editó el {self.model.__name__} correctamente!"
                error = "No hay error!"
                status_code = 201
            else:
                mensaje = f"No se editó el {self.model.__name__} correctamente"
                error = form.errors
                status_code = 400

            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = status_code
            return response
        else:
            return redirect("libro:inicio_autor")        




class EliminarAutor(LoginRequiredMixin, DeleteView):
    model = Autor
    template_name = "libro/autor/eliminar_autor.html"

    def delete(self, request, pk, *args, **kargs):
        if request.is_ajax():
            autor = self.get_object()
            autor.estado = False
            autor.save()    
            mensaje = f"Se eliminó el {self.model.__name__} correctamente!"
            error = "No hay error"
            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = 201
            return response

        return redirect("libro:inicio_autor")

    



class CrearAutor(CreateView):
    form_class = AutorForm
    model = Autor
    success_url = reverse_lazy("libro:listar_autor")
    template_name = "libro/autor/crear_autor.html"

    def post(self, request, *args, **kargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f"El {self.model.__name__} se ha creado correctamente."
                error = "No hay error!"
                status_code = 201
            else:
                mensaje = f"El {self.model.__name__} no se ha podido crear."
                error = form.errors
                status_code = 400

            response = JsonResponse({"mensaje":mensaje, "error":error})
            response.status_code = status_code
            return response   
        
        return redirect("libro:inicio_autor")


# Empiezan las vistas del modelo Libro

class ListarLibro(LoginRequiredMixin,ListView):
    model = Libro
    

    def get(self,request, *args, **kargs):
        if request.is_ajax():
            libros = Libro.objects.filter(estado = True).order_by('-pk')
            return HttpResponse(serialize("json", libros), "application/json")
        
        return redirect("libro:inicio_libro")    
    



class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    

    def post(self, request, *args, **kargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f"El {self.model.__name__} se ha registrado correctamente!"
                error = "No hay error!"
                status_code = 201
            else:
                mensaje = f"El {self.model.__name__} no se ha registrado correctamente"
                error = form.errors
                status_code = 400

            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = status_code
            return response
        
        return redirect("libro:inicio_libro")    


class EditarLibro(LoginRequiredMixin,UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = "libro/libro/editar_libro.html"
    
    def post(self,request,*args, **kargs):
        if request.is_ajax():
            libro_form = self.form_class(request.POST, instance = self.get_object())
            if libro_form.is_valid():
                libro_form.save()
                mensaje = f"El {self.model.__name__} se editó correctamente!"
                error = "No hay error"
                status_code = 201
            else:
                mensaje = f"El {self.model.__name__} no se editó correctamente"
                error = libro_form.errors
                status_code = 400

            response = JsonResponse({"mensaje":mensaje, "error":error})
            response.status_code = status_code
            return response
        
        return redirect("libro:inicio_libro")


class EliminarLibro(LoginRequiredMixin,DeleteView):
    model = Libro
    template_name = "libro/libro/eliminar_libro.html"

    def delete(self, request, *args, **kargs):
        if request.is_ajax():
            libro = self.get_object()
            libro.estado = False
            libro.save()
            mensaje = f"El {self.model.__name__} se eliminó correctamente!"
            error = "No hay error"
            response = JsonResponse({"mensaje": mensaje, "error":error})
            response.status_code = 201
            return response

        return redirect("libro:inicio_libro")    

