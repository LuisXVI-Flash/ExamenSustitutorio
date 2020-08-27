from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html',{
        'titulo':'Inicio',
    })

def libros(request):
    return render(request, 'libros.html',{
        'titulo':'Libros',
    })

def autores(request):
    return render(request, 'autor.html',{
        'titulo':'Autores',
    })

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
