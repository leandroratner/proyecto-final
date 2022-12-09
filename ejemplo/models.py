from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class MVPFamiliares(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.CharField(max_length=200)
    ultimo_trabajo = models.CharField(max_length=100)
    fecha_de_nacimiento = models.CharField(max_length=100)
    def __str__(self):
      return f"{self.nombre}, {self.edad}, {self.ultimo_trabajo}, {self.fecha_de_nacimiento}"