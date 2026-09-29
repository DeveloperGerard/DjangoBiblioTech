from django.shortcuts import render
from .models import Libro
from django.http import HttpResponseNotFound
# Create your views here.


def list_books(request):
    libros = Libro.objects.all()
    
    return render(request,"index.html",{"libros":libros})

def detalle_libro(request,id):
    try:
        libro = Libro.objects.get(id=id)
    except:
        return HttpResponseNotFound("No se encontro el producto")
    return render(request,"libro.html",{"libro":libro})

def categoria_libro(request,categoria):
    try:
        libro = Libro.objects.all()
        
    except:
        return HttpResponseNotFound("No se encontro el producto")
    return render(request,"libro.html",{"libro":libro})