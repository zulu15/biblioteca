from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, include, re_path
from apps.usuario.views import login_view, logout_view
from apps.libro.views import ListarLibrosDisponibles
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libro/', include(('apps.libro.urls','libro'))),
    path("", ListarLibrosDisponibles.as_view() , name = "index"),
    path("accounts/login/", login_view , name = "login"),
    path('logout/', login_required(logout_view), name = "logout"),
    path('usuario/', include(('apps.usuario.urls','usuario'))),
]


urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]