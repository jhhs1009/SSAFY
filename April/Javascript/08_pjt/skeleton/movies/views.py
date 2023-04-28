from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Genre, Movie
from .forms import MovieForm

from django.core.paginator import Paginator

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, "movies/index.html", context)
    

@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movies_form = MovieForm()
    context = {
        'movie' : movie,
        'movies_form' : movies_form,
    }
    return render(request, "movies/detail.html", context)
    


@require_safe
def recommended(request):
    movies = get_list_or_404(Movie)
    m = []
    i=0
    for movie in movies:
        if movie.vote_average > 8.3 and movie.popularity > 30.000:
            i += 1
            m.append([i,movie.title, movie.vote_average,movie.pk, movie.poster_path])
        
    p = Paginator(m, 10)
    page1 = p.page(1).object_list
    context = {
        'page1' : page1
    }
    return render(request, "movies/recommended.html", context)

@require_safe
def list(request, name):
    print(name)
    movies = get_list_or_404(Movie)
    m = []
    i=0
    for movie in movies:
        for genre in movie.genres.all():
            if genre.name == name:
                i += 1
                m.append([i,movie.title, movie.vote_average,movie.pk, movie.poster_path, genre.name])
        
    p = Paginator(m, 10)
    page1 = p.page(1).object_list
    context = {
        'page1' : page1
    }
    return render(request, "movies/list.html", context)


@require_safe
def genre_list(request):
    return render(request, "movies/genre_list.html")
