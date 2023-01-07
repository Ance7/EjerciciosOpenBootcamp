from django.shortcuts import render

from .models import Genero, Director, Peliculas

def index(request):
    cant_directores = Director.objects.all().count()
    cant_peliculas = Peliculas.objects.all().count()
    cant_generos = Genero.objects.all().count()

    return render (
        request,
        'index.html',
        context={
            'cant_directores': cant_directores,
            'cant_peliculas': cant_peliculas,
            'cant_generos': cant_generos

        }
    )