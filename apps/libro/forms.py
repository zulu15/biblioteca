from django import forms
from django.utils.html import escape
from django.core.exceptions import ValidationError

from .models import Autor, Libro, Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = "__all__"

    def clean_libro(self):
        libro = self.cleaned_data["libro"]
        if libro.cantidad < 1:
            raise ValidationError("No se puede reservar este libro, no tiene stock!") 
        return libro

class AutorForm(forms.ModelForm):

    def clean_nombre(self):
        return escape(self.cleaned_data.get('nombre'))       
    
    def clean_apellido(self):
        return escape(self.cleaned_data.get('apellido'))       
    
    def clean_nacionalidad(self):
        return escape(self.cleaned_data.get('nacionalidad'))           
    
    def clean_descripcion(self):
        return escape(self.cleaned_data.get('descripcion'))               
    
    
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

    def clean_titulo(self):
        return escape(self.cleaned_data.get('titulo'))       
    
    def clean_descripcion(self):
        return escape(self.cleaned_data.get('descripcion'))       
    
      
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["autor_id"].queryset = Autor.objects.filter(estado = True)
    
    class Meta:
        model = Libro
        fields = ['titulo','autor_id','fecha_publicacion', 'descripcion', 'cantidad','imagen']
        labels = {
            'titulo':'Ingrese el título del libro',
            'autor_id':'Seleccione los autores del libro',
            'fecha_publicacion':'Indique la fecha de publicación del libro'
        }
        widgets = {
            'titulo':forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese el Título del libro',
                    'class':'form-control',
                    'id':'titulo'
                }
            ),
            'autor_id':forms.SelectMultiple(
                attrs = {
                    'class':'form-control',
                    'id':'autor_id'
                }
            ),
            'fecha_publicacion':forms.SelectDateWidget(
                attrs = {
                    'class':'form-control',
                    'id':'fecha_publicacion'
                }
            ),
            'descripcion': forms.Textarea(attrs={
                'class':'form-control'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class':'form-control'
            })


        }
