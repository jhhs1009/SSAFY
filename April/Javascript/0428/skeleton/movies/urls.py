from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/', views.recommended, name='recommended'),
    path('romance/', views.romance, name='romance'),
    path('drama/', views.drama, name='drama'),
    path('Sf/', views.Sf, name='Sf'),
]
