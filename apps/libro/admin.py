from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .forms import ReservaForm
from .models import Autor, Libro, Reserva
# Register your models here.


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','cantidad','fecha_creacion','estado')

class ReservaAdmin(admin.ModelAdmin):
    form = ReservaForm
    list_display = ('libro','usuario','fecha_creacion','cantidad_dias','estado')

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = ['eliminacion_logica_autores','habilitacion_logica_autores']
    search_fields = ('nombre','apellido','nacionalidad')
    list_display = ('nombre','apellido','nacionalidad','estado')
    resource_class = AutorResource

    def eliminacion_logica_autores(self, request, queryset):
        for autor in queryset:
            autor.estado = False
            autor.save()

    def habilitacion_logica_autores(self, request, queryset):
        for autor in queryset:
            autor.estado = True
            autor.save()

    def get_actions(self,request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions








admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Reserva, ReservaAdmin)
