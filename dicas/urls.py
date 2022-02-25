from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dica_id>', views.dica, name= 'dica')
]