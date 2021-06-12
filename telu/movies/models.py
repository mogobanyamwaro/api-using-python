from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    daily_rate = models.FloatField()
    number_in_stock = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title, self.release_year, self.daily_rate, self.number_in_stock, self.genre, self.date_created
