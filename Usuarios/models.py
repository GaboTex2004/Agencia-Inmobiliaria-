from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, apellidos, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            nombres=nombres,
            apellidos=apellidos
        )
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, nombres, apellidos, password):
        user = self.create_user(
            email=email,
            username=username,
            nombres=nombres,
            apellidos=apellidos,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    username = models.CharField(max_length=50, unique=True)

    estado = models.BooleanField(default=True)

    ultimo_acceso = models.DateTimeField(auto_now=True, null=True, blank=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nombres', 'apellidos']

    def __str__(self):
        return self.email