from django.shortcuts import render
from .models import Film
from django.views.generic import ListView, DetailView, View


class FilmView(ListView):
    queryset = Film.objects.prefetch_related('actor__actors', 'genre').all()
    context_object_name = 'films'
    template_name = 'catalog/list_films.html'

