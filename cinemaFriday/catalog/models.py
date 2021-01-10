from django.db import models
from django.db.models import Avg, Count
from django.contrib.auth.models import User


class Country(models.Model):
    name_county = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name_county


class MovieRole(models.Model):
    role = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.role


class MovieFigure(models.Model):
    fio = models.CharField(max_length=128, null=False)
    role = models.ManyToManyField(MovieRole, related_name='role_figure')

    def __str__(self):
        return self.fio


class Genre(models.Model):
    genre_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.genre_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=32, unique=True)


class Film(models.Model):
    movie_title = models.CharField(max_length=32, unique=True)  # Название фильма
    production_year = models.DateField(null=False)  # Год производства фильма
    country = models.ForeignKey(Country, on_delete=models.PROTECT)  # Страна производства фильма
    image = models.ImageField(upload_to='catalog', blank=True, null=True)  # Обложка фильма
    budget = models.DecimalField(max_digits=8, decimal_places=2)  # Бюджет фильма
    worldwide_gross = models.DecimalField(max_digits=8, decimal_places=2)  # Сборы фильма в мире
    duration = models.DurationField()  # Длительность фильма
    genre = models.ManyToManyField(Genre)  # Жанры фильма
    director = models.ManyToManyField(MovieFigure, related_name='director')  # режисер
    producer = models.ManyToManyField(MovieFigure, related_name='producer')  # продюсер
    actor = models.ManyToManyField(MovieFigure, related_name='actors')  # актеры
    # review = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True, blank=True, related_name='review')  # Отзывы
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.PROTECT)  # Теги к фильмам

    @property
    def rating(self):
       # rating_value = Film.objects.filter(review__film_id=self.id).prefetch_related('review_set').aggregate(Avg('review_set__rating'))
        rating_value = Film.objects.prefetch_related('review_set').filter(review__film_id=self.id).aggregate(Avg('review__rating'))
        return round(rating_value['review__rating__avg'] if rating_value['review__rating__avg'] else 0, 1)

    @property
    def count_review(self):
        count_review = Film.objects.prefetch_related('review_set').filter(review__film_id=self.id).count
        return count_review

    def __str__(self):
        return self.movie_title

    class Meta:
        unique_together = ['movie_title', 'production_year']


class Review(models.Model):
    film_review_title = models.CharField(max_length=256, null=False, blank=False)
    film_review = models.TextField(blank=False)
    rating = models.PositiveSmallIntegerField(null=True, default=0, blank=True)  # Рейтинг
    film = models.ForeignKey(Film, on_delete=models.PROTECT)

    def __str__(self):
        return f"Title: {self.film_review_title}, " \
               f"Review: {self.film_review}"

    class Meta:
        unique_together = ['film_review', 'film_review_title']


class AuthorReview(models.Model):
    fio = models.CharField(max_length=128, null=False, default='')
    review = models.ForeignKey(Review, on_delete=models.PROTECT, related_name='review')

    def __str__(self):
        return self.fio
