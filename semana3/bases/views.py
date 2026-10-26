
# Create your views here.
from django.shortcuts import render
from .models import aprendiz
# Create your views here.

# views.py

def listar_aprendices(request):
    # Consultamos todos los aprendices registrados
    aprendices = aprendiz.objects.all()
    
    # Pasamos el QuerySet dentro del diccionario de contexto
    contexto = {
        'aprendices': aprendices
    }
    
    return render(request, 'bases/lista_aprendices.html', contexto)