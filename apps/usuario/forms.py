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

    def clean_password2(self):
        """ Validacion de contraseña

        Metodo que valida que ambas contraseñas sean iguales, antes de ser guardadas
        y encriptadas en la base de datos. Retorna la contraseña valida

        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password2 != password1:
            raise forms.ValidationError("Las contraseñas no son iguales!")

        return password2

    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password2"])
        user.save()
        return user


    class Meta:
        model = Usuario
        fields = ["username","email","nombres","apellidos"]
        widgets = {
            "username":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Ingrese su nombre de usuario",
                    "id":"username"
                }
            ),
            "email":forms.EmailInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Ingrese su correo electrónico",
                    "id":"email"
                }
            ),
            "nombres":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Ingrese su nombre",
                    "id":"nombres"
                }
            ),
            "apellidos":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Ingrese su apellido",
                    "id":"apellidos"
                }
            )
        }
