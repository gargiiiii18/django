
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

#drf view
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# Create your views here.
def lemon_tea_recipe(request):
    return JsonResponse({"recipe":"Boil water, add tea leaves, sugar, lemon, done!"})

def hello(request):
    return JsonResponse({"message":"Hello!"})
