from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Comment
from .forms import MovieForm, CommentForm


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comments_form' : comments_form,
        'comments' : comments
    }
    return render(request, 'movies/detail.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)



def comments_create(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
        return redirect("movies:detail", movie.pk)
    return redirect("accounts:login")
        

def comments_delete(request,pk,comment_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect("movies:detail", pk)
    

def likes(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect("movies:index")
    return redirect("accounts:login")


def hate(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        if movie.hate_users.filter(pk=request.user.pk).exists():
            movie.hate_users.remove(request.user)
        else:
            movie.hate_users.add(request.user)
        return redirect("movies:index")
    return redirect("accounts:login")