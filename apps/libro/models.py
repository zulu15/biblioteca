from django.db import models

# Create your models here.


class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellido = models.CharField(max_length = 220, blank = False, null = False)
    nacionalidad = models.CharField(max_length = 100, blank = False, null = False)
    descripcion = models.TextField("Descripción", blank = True, null = True)
    fecha_creacion = models.DateField("Fecha de creación", auto_now = True, auto_now_add = False)
    estado = models.BooleanField("Estado", default = True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre + " " + self.apellido
        
    def natural_key(self):
        return f"{self.nombre} {self.apellido}"



class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField("Título", max_length = 255, blank = False, null = False)
    fecha_publicacion = models.DateField("Fecha de publicación", blank = False, null = False)
    #Creamos la relacion
    # Relacion uno a a uno
    autor_id = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField("Fecha de creación", auto_now = True, auto_now_add = False)
    estado = models.BooleanField("Estado Activo/Inactivo", default = True)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
