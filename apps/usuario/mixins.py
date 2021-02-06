from django.shortcuts import redirect


class AuthenticatedYSuperUsuarioMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
    
        return redirect("index")    
    