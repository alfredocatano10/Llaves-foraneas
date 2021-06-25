from django.db import models

class Puesto(models.Model):
   nombre = models.CharField(default = "",null=True,max_length = 50)
   propietario = models.TextField(default = "",null=True,max_length = 50)

class Producto(models.Model):
   puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, default = "",null=True,max_length = 50)
   codigo = models.IntegerField(default = "",null=True,max_length = 50)
   descripcion = models.TextField(default = "",null=True,max_length = 50)

class Reserva(models.Model):
   producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default = "",null=True,max_length = 50)
   cliente = models.CharField(default = "",null=True,max_length = 50)
   fecha = models.DateField(default = "",null=True,max_length = 50)

