from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):

    password1 = forms.CharField(label = "Ingrese su contraseña", widget = forms.PasswordInput(
        attrs = {
            "class":"form-control",
            "placeholder":"Ingrese su contraseña",
            "id":"password1",
            "required":"required"
        }
    ))

    password2 = forms.CharField(label = "Repita su contraseña", widget = forms.PasswordInput(
        attrs = {
            "class":"form-control",
            "placeholder":"Repita su contraseña",
            "id":"password2",
            "required":"required"
        }
    ))


    class Meta:
        model = Usuario
        fields = ["username","email","nombres","apellidos"]
        widgets = {
            "username":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Ingrese su nombre de usuario"
                }
            ),
            "email":forms.EmailInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Ingrese su correo electrónico"
                }
            ),
            "nombres":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Ingrese su nombre"
                }
            ),
            "apellidos":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Ingrese su apellido"
                }
            )
        }
