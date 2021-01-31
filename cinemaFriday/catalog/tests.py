from django.test import TestCase
from .models import Review, AuthorReview, Country, MovieRole, MovieFigure, Genre, Tag, Film
from django.test import Client
from django.urls import reverse


class TestModel(TestCase):
    def setUp(self):
        self.author = AuthorReview.objects.create(fio='Иванов Иван Алексеевич')
        self.country = Country.objects.create(name_county='США')
        self.movie_role = MovieRole.objects.create(role='актер')
        self.genre = Genre.objects.create(genre_name='комедия')
        self.movie_figure = MovieFigure.objects.create(fio='Алексеев Алексей Иванович')
        self.tag = Tag.objects.create(tag_name='лучший фильм 2021')

    def tearDown(self):
        AuthorReview.objects.all().delete()
        Country.objects.all().delete()
        MovieRole.objects.all().delete()
        Genre.objects.all().delete()
        MovieFigure.objects.all().delete()
        Tag.objects.all().delete()

    def test_model_author(self):
        self.assertEqual('Иванов Иван Алексеевич', str(self.author))

    def test_model_country(self):
        self.assertEqual('США', str(self.country))

    def test_model_movie_role(self):
        self.assertEqual('актер', str(self.movie_role))

    def test_model_genre(self):
        self.assertEqual('комедия', str(self.genre))

    def test_model_movie_figure(self):
        self.assertEqual('Алексеев Алексей Иванович', str(self.movie_figure))

    def test_model_tag(self):
        self.assertEqual('лучший фильм 2021', str(self.tag.tag_name))


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_index(self):
        url = reverse('catalog:about')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_context_paginate(self):
        response = self.client.get('/')
        self.assertEqual(response.context['is_paginated'], False)

    def test_page_not_found(self):
        response = self.client.get('/test')
        self.assertEqual(404, response.status_code)
