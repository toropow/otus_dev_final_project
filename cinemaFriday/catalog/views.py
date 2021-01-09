from django.shortcuts import render
from .models import Film, Review
from django.views.generic import ListView, DetailView, CreateView


class FilmView(ListView):
    queryset = Film.objects.prefetch_related('actor__actors', 'genre', 'review_set').all()
    context_object_name = 'films'
    template_name = 'catalog/list_films.html'

    # def get_queryset(self):
    #     queryset = {'all_films': Film.objects.prefetch_related('actor__actors', 'genre').all(),
    #                 'review': Review.objects.select_related('film').all()}
    #     return queryset

class FilmDetailView(DetailView):
    queryset = Film.objects.prefetch_related('actor__actors', 'genre').all()
    context_object_name = 'film'
    template_name = 'catalog/film_detail.html'


class ReviewCreateView(CreateView):
    model = Review
    template_name = 'catalog/create_review.html'
    success_url = '/'
    fields = '__all__'



