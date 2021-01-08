from django.core.management.base import BaseCommand, CommandError
from catalog.models import Country, MovieRole, MovieFigure, Genre, AuthorReview, Review, Film



class Command(BaseCommand):
    help = "Upload data"

    def handle(self, *args, **kwargs):
        print('------ delete old data')
        Country.objects.all().delete()
        MovieRole.objects.all().delete()
        MovieFigure.objects.all().delete()
        Genre.objects.all().delete()
        AuthorReview.objects.all().delete()
        Review.objects.all().delete()
        Film.objects.all().delete()

        print("------ upload data: start")

        print("------ upload Country")
        country_usa = Country.objects.create(name_county='США')
        country_france = Country.objects.create(name_county='Франция')
        country_japan = Country.objects.create(name_county='Япония')
        country_italy = Country.objects.create(name_county='Италия')
        country_uk = Country.objects.create(name_county='Великобритания')

        print("------ upload MovieRole")
        role_director = MovieRole.objects.create(role='режисер')
        role_producer = MovieRole.objects.create(role='продюсер')
        role_actor = MovieRole.objects.create(role='актер')

        print("------ upload MovieFigure")
        # TODO: add data

        print("------ upload Genre")
        genre_drama = Genre.objects.create(genre_name='драма')
        genre_comedy = Genre.objects.create(genre_name='комедия')
        genre_action = Genre.objects.create(genre_name='боевик')
        genre_romance = Genre.objects.create(genre_name='мелодрама')
        genre_thriller = Genre.objects.create(genre_name='триллер')

        print("------ upload AuthorReview")
        author_review_petrov = AuthorReview.objects.create(fio='Петров Иван Сергеевич')
        author_review_ivanov = AuthorReview.objects.create(fio='Иванов Андрей Сергеевич')
        author_review_samoletov = AuthorReview.objects.create(fio='Самолетов Дмитрий Андреевич')

        print("------ upload Review")

        review_first = Review.objects.create(
            film_review_title="Хороший фильм",
            film_review="Мне понравился, стоит посмотреть. Захватывающий сюджет",
            author_review=author_review_petrov
        )

        review_second = Review.objects.create(
            film_review_title="Не плохой фильм",
            film_review="Можно посмотреть один раз",
            author_review=author_review_ivanov
        )

        review_third = Review.objects.create(
            film_review_title="Не рекомендую",
            film_review="Фильм, совсем не понравился, жалко потраченного времени",
            author_review=author_review_samoletov
        )



        print("------ upload Film")




        print("------ upload data: end")
