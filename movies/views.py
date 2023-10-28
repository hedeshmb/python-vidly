from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([movie.title for movie in movies])
    # Movie.objects.filter(release_year=1200)
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except:
    #     raise Http404()

    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
