
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('noticia/<int:pk>/', views.detalle_noticia, name='detalle_noticia'),
]