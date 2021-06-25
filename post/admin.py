from django.contrib import admin
from .models import Puesto, Producto, Reserva

Model = Puesto, Producto, Reserva

admin.site.register(Model)
