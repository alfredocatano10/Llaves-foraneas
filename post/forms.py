from django import forms
from .models import Puesto, Producto, Reserva


class postForm (forms.ModelForm):
	
	class Meta:
		model = Puesto
		fields = '__all__'

