from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Libro, Autor, Editoriales, Pais

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
    editoriales = Editoriales.objects.all()
    return render(request, 'editorial.html',{
        'titulo':'Editoriales',
        'editoriales':editoriales
    })

def eliminar_editoriales(request, id):
    editoriales = Editoriales.objects.get(pk=id)
    editoriales.delete()
    return redirect("editoriales")

def paises(request):
    paises = Pais.objects.all()
    return render(request, 'pais.html',{
        'titulo':'Paises',
        'paises':paises
    })
    
def eliminar_paises(request, id):
    paises = Pais.objects.get(pk=id)
    paises.delete()
    return redirect("paises")

def consultas(request):
    return render(request, 'consultas.html',{
        'titulo':'Consultas',
    })
