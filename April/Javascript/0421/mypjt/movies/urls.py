from django.urls import path
from movies import views

urlpatterns = [
    path('actors/', views.actors_list),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('movies/', views.movies_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('reviews/', views.reviews_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/', views.create_review),
]
