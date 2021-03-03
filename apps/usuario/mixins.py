from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


class LoginYStaffMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
    
        return redirect("index")    


class LoginYSuperUserMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
        
        messages.error(request, 'Usted no tiene permisos para realizar esta acción!.')
        return redirect("login")    





class ValidarPermisosUsuarioMixin(object):
    permission_required =  ('usuario.view_usuario', 'usuario.add_usuario', 'usuario.change_usuario', 'usuario.delete_usuario' )
    url_redirect = None


    def get_perms(self):
        if isinstance(self.permission_required, str):
            return (self.permission_required)
        else:
            return self.permission_required    


    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy("login")
        else:
            return self.url_redirect

    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request, 'Usted no tiene permisos para realizar esta acción!.')
            return redirect(self.get_url_redirect())    
            
                        