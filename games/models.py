from django.db import models
from django.db.models.functions import Now


class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Personaje(models.Model):
    raza = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    nivel = models.IntegerField(default=0)
    ban = models.BooleanField(default=False)
    creado = models.DateTimeField(default=Now)

    def __str__(self):
        return f"{self.raza}  nivel {self.nivel}"


class Item(models.Model):
    personaje = models.ForeignKey( Personaje, on_delete=models.CASCADE)
    categoria = models.ForeignKey( Categoria, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return self.nombre


class Cuenta(models.Model):
    usuario = models.CharField(max_length=80, unique=True)
    correo = models.CharField(max_length=120)

    def __str__(self):
        return self.usuario


class CuentaPersonaje(models.Model):
    cuenta = models.ForeignKey( Cuenta, on_delete=models.CASCADE)
    personaje = models.ForeignKey( Personaje, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cuenta.usuario} {self.personaje.id}"
# Create your models here.
