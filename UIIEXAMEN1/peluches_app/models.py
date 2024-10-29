from django.db import models

class Sucursal(models.Model):
    id_sucursal=models.CharField(primary_key=True,max_length=10)
    direccion=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    id_empleado=models.CharField(max_length=10)
    horario=models.CharField(max_length=20)
    correo=models.CharField( max_length=50)

    def __str__(self):
     return self.nombre

