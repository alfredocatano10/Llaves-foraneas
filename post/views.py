from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Puesto, Producto, Reserva
from .forms import postForm

# Create your views here.
#---------------------------------------------------------------
#---------------------------------------------------------------

class HomePageView(ListView):
	model = Puesto
	template_name = 'home.html'

class PostPageView(ListView):
	model = Puesto
	template_name = 'post.html'
	context_object_name = 'post_list'


#---------------------------------------------------------------
#---------------------------------------------------------------

def agregar (request):
	
	data = {
		'form':postForm()
	}

	if request.method == 'POST':
		formulario = postForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='post')
		else:
			data['form'] = formulario

	return render(request, 'agregar.html',data)
