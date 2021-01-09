from django.core.management.base import BaseCommand, CommandError
from catalog.models import Country, MovieRole, MovieFigure, Genre, AuthorReview, Review, Film
import factory
from random import randint
from datetime import timedelta


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name_county = factory.Faker('country')


class MovieRoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MovieRole

    role = factory.Iterator(['режисер', 'продюсер', 'актер'])


class MovieFigureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MovieFigure

    fio = factory.Faker('name_nonbinary')

    @factory.post_generation
    def role(self, create, extracted, **kwargs):
        if extracted:
            for rol in extracted:
                self.role.add(rol)


class AuthorReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AuthorReview

    fio = factory.Faker('name_nonbinary')
    review = factory.Iterator(Review.objects.all())


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    film_review_title = factory.Faker('sentence', nb_words=3)
    film_review = factory.Faker('sentence', nb_words=20)
    #author_review = factory.Iterator(AuthorReview.objects.all())
    rating = factory.Iterator([randint(1, 10) for x in range(100)])
    film = factory.Iterator(Film.objects.all())


class FilmFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Film

    movie_title = factory.Faker('sentence', nb_words=3)
    production_year = factory.Faker('date')
    country = factory.Iterator(Country.objects.all())
    image = 'catalog/cinema.jpeg'
    budget = factory.Iterator([float(randint(1000, 100000)) for x in range(100)])
    worldwide_gross = factory.Iterator([float(randint(1000, 100000)) for x in range(100)])
    duration = factory.Iterator([timedelta(minutes=randint(30, 180)) for x in range(100)])

    # review = factory.SubFactory(ReviewFactory)

    @factory.post_generation
    def genre(self, create, extracted, **kwargs):
        if extracted:
            for ge in extracted:
                self.genre.add(ge)

    #
    # @factory.post_generation
    # def review(self, create, extracted, **kwargs):
    #     if extracted:
    #         for rev in extracted:
    #             self.review.add(rev)

    @factory.post_generation
    def director(self, create, extracted, **kwargs):
        if extracted:
            for dir in extracted:
                self.director.add(dir)

    @factory.post_generation
    def producer(self, create, extracted, **kwargs):
        if extracted:
            for prod in extracted:
                self.producer.add(prod)

    @factory.post_generation
    def actor(self, create, extracted, **kwargs):
        if extracted:
            for act in extracted:
                self.actor.add(act)

    @factory.post_generation
    def tag(self, create, extracted, **kwargs):
        if extracted:
            for tg in extracted:
                self.tag.add(tg)


def delete_all():
    MovieRole.objects.all().delete()
    MovieFigure.objects.all().delete()
    Review.objects.all().delete()
    Genre.objects.all().delete()
    AuthorReview.objects.all().delete()
    Film.objects.all().delete()
    Country.objects.all().delete()


class Command(BaseCommand):
    help = "Upload data"

    def handle(self, *args, **kwargs):
        print('------ delete old data')
        delete_all()
        print("------ upload data: start")

        print("------ upload Country")
        countries = CountryFactory.create_batch(5)
        for county in countries:
            print(county.name_county)

        print("------ upload MovieRole")
        roles = MovieRoleFactory.create_batch(3)
        for rl in roles:
            print(rl.role)

        print("------ upload MovieFigure")
        # Создадим 5 режиссеров
        figures = MovieFigureFactory.create_batch(5, role=MovieRole.objects.filter(role='режисер'))
        for figure in figures:
            print(figure)

        # Создадим 5 актеров
        figures = MovieFigureFactory.create_batch(5, role=MovieRole.objects.filter(role='актер'))
        for figure in figures:
            print(figure)

        # Создадим 5 продюссеров
        figures = MovieFigureFactory.create_batch(5, role=MovieRole.objects.filter(role='продюсер'))
        for figure in figures:
            print(figure)

        print("------ upload Genre")
        genre_drama = Genre.objects.create(genre_name='драма')
        genre_comedy = Genre.objects.create(genre_name='комедия')
        genre_action = Genre.objects.create(genre_name='боевик')
        genre_romance = Genre.objects.create(genre_name='мелодрама')
        genre_thriller = Genre.objects.create(genre_name='триллер')

        print("------ upload Film")

        films = FilmFactory.create_batch(
            10,
            genre=Genre.objects.all(),
            director=MovieFigure.objects.prefetch_related('role').filter(role__role='режисер').all(),
            producer=MovieFigure.objects.prefetch_related('role').filter(role__role='продюсер').all(),
            actor=MovieFigure.objects.prefetch_related('role').filter(role__role='актер').all(),
            #  review=Review.objects.all()
        )

        for film in films:
            print(film)

        print("------ upload Review")
        reviews = ReviewFactory.create_batch(5)
        for review in reviews:
            print(review)

        print("------ upload AuthorReview")
        authors_review = AuthorReviewFactory.create_batch(5)
        for author in authors_review:
            print(author)

        print("------ upload data: end")
