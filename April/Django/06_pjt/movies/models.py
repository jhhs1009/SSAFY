from django.db import models
from django.conf import settings


class Movie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hate_movies')
    title = models.CharField(max_length=20)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content