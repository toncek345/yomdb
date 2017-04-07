from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre_text = models.CharField(max_length=50)

    def __str__(self):
        return self.genre_text


class Movie(models.Model):
    title = models.CharField(max_length=200)
    watched = models.BooleanField(default=False)
    time_added = models.DateTimeField()

    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

# Create your models here.
