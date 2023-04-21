from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Actor, Movie, Review
from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer,ActorDetailSerializer,MovieDetailSerializer, ReviewDetailSerializer

from rest_framework import status

@api_view(['GET'])
def actors_list(request):
    if request.method == "GET":
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def actor_detail(reqeust,actor_pk):
    if reqeust.method == "GET":
        actor = get_object_or_404(Actor, pk=actor_pk)
        serializer = ActorDetailSerializer(actor)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def movies_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data) 
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == "GET":
        actor = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieDetailSerializer(actor)
        return Response(serializer.data)
    
@api_view(['GET'])    
def reviews_list(request):
    if request.method == "GET":
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE']) 
def review_detail(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    
    if request.method == "GET":
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method=="DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def create_review(request, movie_pk):
    if request.method == "POST":
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        movie_ = movie.review_set.all()
        serializer = ReviewSerializer(movie_, many=True)
        return Response(serializer.data)