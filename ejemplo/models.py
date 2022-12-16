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
    fecha_de_nacimiento = models.CharField(max_length=100) #models.DateField (input__formats"%d-%m-%Y'")
    def __str__(self):
      return f"{self.nombre}, {self.edad}, {self.ultimo_trabajo}, {self.fecha_de_nacimiento}"

class Vehiculo(models.Model):
  tipo = models.CharField(max_length=20)
  color = models.CharField(max_length=20)
  año_modelo = models.CharField(max_length=4)
  def __str__(self):
    return f"{self.tipo}, {self.color}, {self.año_modelo}"

class Mascota(models.Model):
  tipo_animal = models.CharField(max_length=15)
  edad = models.CharField(max_length=2)
  def __str__(self):
    return f"{self.tipo_animal}, {self.edad}"

class Vacaciones(models.Model):
  destino = models.CharField(max_length=15)
  dias_de_estadia = models.CharField(max_length=3)
  def __str__(self):
    return f"{self.destino}, {self.dias_de_estadia}"

