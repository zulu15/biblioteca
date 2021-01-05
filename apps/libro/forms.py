from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre","apellido","nacionalidad","descripcion"]
        labels = {
            'nombre':'Ingrese el nombre',
            'apellido':'Ingrese el apellido',
            'nacionalidad':'Ingrese la nacionalidad',
            'descripcion':'Ingrese una pequeña descripcion',
        }

        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                    'id':'nombre',
                    'class':'form-control',
                    'placeholder':'Nombre del autor'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'id':'apellido',
                    'class':'form-control',
                    'placeholder':'Apellido del autor'
                }
            ),
            'nacionalidad':forms.TextInput(
                attrs = {
                    'id':'nacionalidad',
                    'class':'form-control',
                    'placeholder':'Nacionalidad del autor'
                }
            ),
            'descripcion':forms.Textarea(
                attrs = {
                    'id':'descripcion',
                    'class':'form-control',
                    'placeholder':'Pequeña descripción del autor'
                }
            ),

        }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo','autor_id','fecha_publicacion']
        labels = {
            'titulo':'Ingrese el título del libro',
            'autor_id':'Seleccione los autores del libro',
            'fecha_publicacion':'Indique la fecha de publicación del libro'
        }
        widgets = {
            'titulo':forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese el Título del libro',
                    'class':'form-control'
                }
            ),
            'autor_id':forms.SelectMultiple(
                attrs = {
                    'class':'form-control'
                }
            ),
            'fecha_publicacion':forms.SelectDateWidget(
                attrs = {
                    'class':'form-control'
                }
            )

        }