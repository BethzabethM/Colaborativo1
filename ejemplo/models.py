from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.fecha_nacimiento}, {self.id}"


class Vivienda(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_casa = models.CharField(max_length=100)
    habitaciones = models.IntegerField()
    baños = models.IntegerField()
    descripcion = models.CharField(max_length=1000)


class Datos(models.Model):
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=500)
    hobbie =  models.CharField(max_length=100)
    deporte =  models.CharField(max_length=100)


class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    construido_por = models.CharField(max_length=30, default='')
    titulo_principal = models.CharField(max_length=30, default='')
    subtitulo_principal = models.CharField(max_length=60, default='')
