from django.contrib.auth.models import User
from django.db import models


class IMDB(models.Model):
    popularity = models.FloatField(db_column="99popularity", blank=False, )
    director = models.CharField(max_length=30, blank=False)
    genre = models.CharField(max_length=100, blank=False)
    imdb_score = models.FloatField(blank=False)
    name = models.CharField(max_length=50, blank=False, unique=True)
