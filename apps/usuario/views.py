import json
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
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



class ListarUsuario(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "usuario/listar_usuario.html"
    queryset = Usuario.objects.filter(is_active = True)

    def get(self, request, *args, **kargs):
        if request.is_ajax():
            lista_usuarios = self.queryset
            return HttpResponse(serialize('json', lista_usuarios), 'application/json')
        else:
            return redirect("usuario:inicio_usuario")

class EliminarUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy("usuario:listar_usuario")

    def post(self,request,pk,*args,**kargs):
        usuario = get_object_or_404(self.Model, pk = pk)
        usuario.is_active = False
        usuario.save()
        return redirect(self.success_url)

    def get_object(self, queryset=None):
        """ Hook to ensure object is not admin. """
        obj = super(EliminarUsuario, self).get_object()
        if obj.is_admin:
            raise PermissionDenied("No está permitido eliminar usuarios administradores")

        return obj


class EditarUsuario(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy("usuario:listar_usuario")
    template_name = "usuario/editar_usuario.html"