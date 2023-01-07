from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=20, help_text="Nombre del genero")

    def __str__(self):
        return self.nombre

 
class Director(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre del director")
    edad = models.IntegerField()
    nacimiento = models.DateField()
    fallecimiento = models.DateField(blank=True)
    
    def __str__(self):
        return self.nombre

class Peliculas(models.Model):
    nombre = models.CharField(max_length=30, help_text="Nombre de pelicula")
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    genero = models.ManyToManyField(Genero)
    
    def __str__(self):
        return self.nombre
 