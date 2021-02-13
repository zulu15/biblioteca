from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Usuario

# Register your models here.

admin.site.register(Permission)
admin.site.register(Usuario)
