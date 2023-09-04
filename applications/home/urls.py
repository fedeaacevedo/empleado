
from django.urls import path
from . import views

urlpatterns = [
 
    path('home/', views.IndexView.as_view()),
    path('lista-prueba/', views.ModeloPrueba.as_view())
]
