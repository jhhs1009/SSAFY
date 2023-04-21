from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)

    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date= models.DateTimeField(auto_now=True)
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor)
    
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)