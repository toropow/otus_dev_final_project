from django.shortcuts import render
from .models import Film, Review
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User


class AboutView(TemplateView):
    template_name = 'catalog/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data()
        context['active_page'] = '/about/'
        return context


class FilmView(ListView):
    queryset = Film.objects.prefetch_related('actor__actors', 'genre', 'review_set').all()
    context_object_name = 'films'
    template_name = 'catalog/list_films.html'


class FilmDetailView(DetailView):
    queryset = Film.objects.prefetch_related('actor__actors', 'genre', 'review_set').all()
    context_object_name = 'film'
    template_name = 'catalog/film_detail.html'


class ReviewCreateView(CreateView):
    model = Review
    template_name = 'catalog/create_review.html'
    success_url = '/'
    fields = '__all__'


class FilmCreateView(CreateView):
    model = Film
    template_name = 'catalog/create_film.html'
    success_url = '/'
    fields = '__all__'


class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'catalog/register.html'


class LoginUserView(LoginView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'catalog/login.html'


class LogoutUserView(LogoutView):
    pass
