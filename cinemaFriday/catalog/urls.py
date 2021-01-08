from django.contrib import admin
from django.urls import path
from .views import FilmView

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FilmView.as_view(), name='index'),
]
