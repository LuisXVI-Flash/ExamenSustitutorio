"""proyectouwu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('libros/',views.libros, name="libros"),
    path('eliminar_libros/<int:id>', views.eliminar_libros, name="eliminar_libros"),
    path('autores/',views.autores, name="autores"),
    path('eliminar_autores/<int:id>', views.eliminar_autores, name="eliminar_autores"),
    path('editoriales/',views.editoriales,name="editoriales"),
    path('eliminar_editoriales/<int:id>', views.eliminar_editoriales, name="eliminar_editoriales"),
    path('paises/',views.paises, name="paises"),
    path('eliminar_paises/<int:id>', views.eliminar_paises, name="eliminar_paises"),
    path('consultas/',views.consultas,name="consultas"),

]
