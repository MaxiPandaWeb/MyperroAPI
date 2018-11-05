from django.db import models

class Contacto(models.Model):
    email = models.EmailField()
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    telefono = models.IntegerField()
    region = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    tipo_vivienda = models.CharField(max_length=100)

    def __str__(self):
        return self.rut

class Nuevo(models.Model):
    nom= models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='media')
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

# Create your models here.
