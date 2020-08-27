from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Libro, Autor

# Create your views here.

def index(request):
    return render(request, 'index.html',{
        'titulo':'Inicio',
    })

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros.html',{
        'titulo':'Libros',
        'libros': libros,
    })

def eliminar_libros(request,id):
    libros = Libro.objects.get(pk=id)
    libros.delete()
    return redirect("libros")

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'autor.html',{
        'titulo':'Autores',
        'autores':autores
    })

def eliminar_autores(request, id):
    autores = Autor.objects.get(pk=id)
    autores.delete()
    return redirect("autores")

def editoriales(request):
    return render(request, 'editorial.html',{
        'titulo':'Editoriales',
    })

def paises(request):
    return render(request, 'pais.html',{
        'titulo':'Paises',
    })
    
def consultas(request):
    return render(request, 'consultas.html',{
        'titulo':'Consultas',
    })
