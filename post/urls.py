from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from .views import HomePageView, PostPageView, agregar

urlpatterns = [
	path('',HomePageView.as_view(),name = 'home'),
	path('post/',PostPageView.as_view(), name = 'post'),
	path('agregar/',agregar, name = 'agregar'),
]