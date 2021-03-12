from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','username','nombres','apellidos','is_active','is_staff')

admin.site.register(Permission)
admin.site.register(Usuario, UsuarioAdmin)
