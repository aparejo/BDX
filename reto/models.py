from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Agrega el argumento related_name en los campos groups y user_permissions
    groups = models.ManyToManyField('auth.Group', related_name='reto_users', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='reto_users', blank=True)

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)

class UsuarioSucursal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    password = models.CharField(max_length=128)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, default=1)
    
class Participante(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    cedula = models.CharField(max_length=15)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    puntos = models.IntegerField()
    fecha = models.DateField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default=1)

