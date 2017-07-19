#!/usr/bin/python36
__author__ = "Edu Santos PAZ"
__copyright__ = "Copyright 2017"
__credits__ = ["Emanuel Mendez", "Oscar Luis Sanchez"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Edu Santos PAZ"
__email__ = "eduardo@edsantoshn.com"
__status__ = "Development"

from django.db import models
'''El modulo models.py es donde se crea el modelo de la base de datos, cada clase corresponde a un modelo de tabla'''
# Create your models here.
class Author(models.Model):
	name=models.CharField(max_lenght=30,help_text='Escriba el nombre del autor')
	surname = models.CharField(max_lenght=30,help_text='Escriba el apellido del autor')
	Bday = models.DateField(help_text='Seleccione la fecha de nacimiento')
	email = models.EmailField(help_text='Escriba el email de contacto del autor')

class post(models.Model):
	'''Existen diferentes tipos de archivos, opciones y caracteristicas de cada campo y tipo de dato
	el tipo CharField corresponde a una cadena de texto corta, max_lenght el maximo de caracteres aceptados(No aplica para Integer)
	help_text corresponde al texto de ayuda que se muestra en el admin site'''
	title = models.CharField(max_lenght=60,help_text='Escriba el nombre de la publicación')
	detail = models.CharField(max_lenght=2000, help_text='Escriba la publicación')
	pubdate = models.DateTimeField(auto_now=True)
	author = models.ForiegnKey(Author,help_text='Seleccione al autor')

class comment(models.Model):
	 post=models.ForiegnKey(post,help_text='Seleccione la publicación')
	 comment = models.CharField(max_lenght=1000,help_text='Escriba su comentario')
	 pubdate=models.DateTimeField(auto_now=True)
	 