from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    output = ', '.join([movie.title for movie in movies])
    # Movie.objects.filter(release_year=1200)
    return HttpResponse(output)
