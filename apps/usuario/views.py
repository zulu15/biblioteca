import json
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_param = request.GET.get("next", False)
            return redirect(next_param if next_param else 'index')
        else:
            return render(request, 'login.html', {'username':username,'error':'Usuario y/o contraseña incorrecta'})
    return render(request, template_name = 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


class CrearUsuario(LoginRequiredMixin, CreateView):
    form_class = UsuarioForm
    model = Usuario
    success_url = reverse_lazy("usuario:listar_usuario")
    template_name = "usuario/crear_usuario.html"

    def post(self, request, *args, **kargs):
        if request.is_ajax():
            usuario_form = self.form_class(request.POST)
            if usuario_form.is_valid():
                usuario_form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = "No hay error!"
                response = JsonResponse({"mensaje":mensaje, "error": error})
                response.status_code = 201
                return response
            else:
                mensaje = f' El {self.model.__name__} no se ha registrado correctamente '
                error = usuario_form.errors
                response = JsonResponse({"mensaje":mensaje, "error": error})
                response.status_code = 400
                return response
        else:
            return redirect("usuario:inicio_usuario")



class ListarUsuario(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/listar_usuario.html"
    queryset = Usuario.objects.filter(is_active = True).all()

    def get(self, request, *args, **kargs):
        if request.is_ajax():
            lista_usuarios = Usuario.objects.filter(is_active = True).order_by("-id")
            return HttpResponse(serialize('json', lista_usuarios), 'application/json')
        else:
            return redirect("usuario:inicio_usuario")

class EliminarUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy("usuario:listar_usuario")

    def post(self,request,pk,*args,**kargs):
        usuario = self.get_object()
        usuario.is_active = False
        usuario.save()
        return redirect(self.success_url)

    def get_object(self, queryset=None):
        """ Hook to ensure object is not admin. """
        obj = super(EliminarUsuario, self).get_object()
        if obj.is_admin:
            raise PermissionDenied("No está permitido eliminar usuarios administradores")
        return obj

    def get(self, request, pk, *args, **kargs):
        if request.is_ajax():
            usuario = get_object_or_404(self.model, pk = pk)
            if usuario.is_admin:
                error = "No tiene el permiso para eliminar usuarios administradores"
                mensaje = f' El {self.model.__name__} no se pudo eliminar'
                status_code = 403
            else:
                usuario.is_active = False
                usuario.save()
                mensaje = f' El {self.model.__name__} se eliminó correctamente'
                error = "No hay error"
                status_code = 200


            response = JsonResponse({"mensaje":mensaje, "error":error})
            response.status_code = status_code
            return response
        else:
            return redirect("usuario:inicio_usuario")



class EditarUsuario(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/editar_usuario.html"

    def post(self,request,*args,**kargs):
        if request.is_ajax():
            form_usuario = self.form_class(request.POST, instance = self.get_object())
            if form_usuario.is_valid():
                form_usuario.save()
                error = "No hay error!"
                mensaje = f' El {self.model.__name__} se actualizó correctamente'
                status_code = 201
            else:
                error = form_usuario.errors
                mensaje = f' El {self.model.__name__} no se pudo actualizar'
                status_code = 400

            response = JsonResponse({"mensaje": mensaje, "error": error})
            response.status_code = status_code
            return response
        else:
            return redirect("usuario:inicio_usuario")
