# pops/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('consultar-pops/', views.consultar_pops, name='consultar_pops'),
]
