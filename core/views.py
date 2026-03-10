from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    lista = Producto.objects.all() 
    return render(request, 'core/lista.html', {'productos': lista})