#!/usr/bin/python36
__author__ = "Edu Santos PAZ"
__copyright__ = "Copyright 2017"
__credits__ = ["Emanuel Mendez", "Oscar Luis Sanchez"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Edu Santos PAZ"
__email__ = "eduardo@edsantoshn.com"
__status__ = "Development"

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import date, datetime
from django.views import generic

#Importamos todos los modelos creados en models.py (author,post,comment)
from .models import *

# Create your views here.

class AuthorsIndex(generic.ListView):
    """Enlista a todos los autores registrados"""
    template_name = 'authors/index.html'
    context_object_name = 'authors_context'

    def get_queryset(self):
        """Retorna todos los autores"""
        return author.objects.all()

class PostsIndex(generic.ListView):
    """Enlista a todas publicaciones"""
    template_name = 'posts/index.html'
    context_object_name = 'posts_context'

    def get_queryset(self):
        """Retorna todas las publicaciones"""
        return post.objects.all()

class PostDetail(generic.DetailView):
    """Muestra un post en especifico"""
    model = post
    template_name = 'posts/post.html'
    def get_queryset(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return post.objects.filter(id=pk)

class AuthorPosts(generic.DetailView):
    """Enlista las publicaciones de un autor en especifico"""
    model = post
    template_name = 'posts/authorposts.html'
    def get_queryset(self):
        fk = self.kwargs.get(self.pk_url_kwarg)
        return post.objects.filter(author=fk)

class CommentsPost(generic.DetailView):
    """Enlista los comentarios de una publicación en especifico"""
    model = comment
    template_name = 'posts/allcomments.html'
    def get_queryset(self):
        fk = self.kwargs.get(self.pk_url_kwarg)
        return comment.objects.filter(post=fk)