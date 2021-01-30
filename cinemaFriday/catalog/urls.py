from django.contrib import admin
from django.urls import path
from .views import FilmView, FilmDetailView, ReviewCreateView, AboutView, FilmCreateView, UserCreateView, LoginUserView,\
LogoutUserView


app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FilmView.as_view(), name='index'),
    path('<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('create/', ReviewCreateView.as_view(), name='create'),
    path('create_film/', FilmCreateView.as_view(), name='create_film'),
    path('about/', AboutView.as_view(), name='about'),
    path('registration/', UserCreateView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
