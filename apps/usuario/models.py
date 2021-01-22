from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UsuarioManager(BaseUserManager):

    def create_user(self, username, email, nombres, apellidos, password = None):
            if not email:
                raise ValueError("El usuario debe tener un correo electrónico!")

            usuario = self.model(
                username = username,
                email = self.normalize_email(email),
                nombres = nombres,
                apellidos = apellidos
            )
            #Metodo propio de AbstractBaseUser que encripta la contraseña
            usuario.set_password(password)
            usuario.save()
            return usuario

    #metodo que es invocado al utilizar el comando manage,py createsuperuser
    #los parametros a utilizar aqui deben estar indicados en el campo
    #REQUIRED_FIELDS de lo contrario deben ser del tipo null como apellidos
    #ya que tendremos error al utilizar parametros que no existen
    def create_superuser(self, username, email, nombres, password,  apellidos = None):
        usuario = self.create_user(
            username = username,
            email = email,
            nombres = nombres,
            apellidos = apellidos,
            password = password
        )

        usuario.is_admin = True
        usuario.save()
        return usuario



class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario',unique = True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254,unique = True)
    nombres = models.CharField('Nombres', max_length=200, blank = True, null = False, default = "")
    apellidos = models.CharField('Apellidos', max_length=200,blank = True, null = False, default = "")
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', max_length=200,blank = True,null = True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)

    #Vinculamos nuestro modelo a nuestro propio Manager
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres']



    def __str__(self):
        return self.nombres


    def has_perm(self,perm, obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
