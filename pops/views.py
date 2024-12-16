# pops/views.py
from django.shortcuts import render

def consultar_pops(request):
    # Lógica da view, pode ser uma renderização de template ou outro tipo de resposta
    return render(request, 'consultar_pops.html')
