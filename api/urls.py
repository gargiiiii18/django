from django.urls import path
from .views import lemon_tea_recipe, hello, movie_list

urlpatterns = [
    path('lemon-tea/', lemon_tea_recipe),
    path('hello/', hello),
    path('movies/', movie_list),
]